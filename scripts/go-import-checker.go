// go-import-checker validates the Longhorn Go import ordering convention.
//
// Usage:
//
//	go run go-import-checker.go [--] [file.go ...]
//
// Arguments starting with "-" are ignored, so "--" can be used to separate
// "go run"'s own flags from the file list without causing go run to treat
// the listed .go files as additional source files to compile.
//
// When no files are given, changed files are detected from jj or git.
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strings"
)

// Import group constants — lower value must appear first in the file.
const (
	gStdlib  = 0 // standard library
	gThird   = 1 // third-party (non-k8s, non-longhorn)
	gK8sNoAs = 2 // k8s.io without alias
	gK8sAs   = 3 // k8s.io with alias
	gLhExt   = 4 // github.com/longhorn/* — external repos (any alias)
	gLhCurr  = 5 // current module packages (any alias)
)

var groupNames = [...]string{
	gStdlib:  "stdlib",
	gThird:   "third-party (non-k8s)",
	gK8sNoAs: "k8s.io (no alias)",
	gK8sAs:   "k8s.io (aliased)",
	gLhExt:   "longhorn external",
	gLhCurr:  "current repo",
}

// findModule walks parent directories of filePath until it finds a go.mod,
// then returns the declared module path.
func findModule(filePath string) string {
	dir := filepath.Dir(filePath)
	if !filepath.IsAbs(dir) {
		cwd, err := os.Getwd()
		if err != nil {
			return ""
		}
		dir = filepath.Join(cwd, dir)
	}
	for {
		f, err := os.Open(filepath.Join(dir, "go.mod"))
		if err == nil {
			scanner := bufio.NewScanner(f)
			for scanner.Scan() {
				if mod, ok := strings.CutPrefix(strings.TrimSpace(scanner.Text()), "module "); ok {
					_ = f.Close()
					return strings.TrimSpace(mod)
				}
			}
			_ = f.Close()
			return ""
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			break
		}
		dir = parent
	}
	return ""
}

// classify returns the group constant for a single import.
func classify(importPath, alias, currentModule string) int {
	isAliased := alias != "" && alias != "_" && alias != "."

	firstSeg, _, _ := strings.Cut(importPath, "/")

	// stdlib: no dot in first path segment.
	if !strings.ContainsRune(firstSeg, '.') {
		return gStdlib
	}

	if firstSeg == "k8s.io" {
		if isAliased {
			return gK8sAs
		}
		return gK8sNoAs
	}

	if currentModule != "" && (importPath == currentModule || strings.HasPrefix(importPath, currentModule+"/")) {
		return gLhCurr
	}

	if strings.HasPrefix(importPath, "github.com/longhorn/") {
		return gLhExt
	}

	return gThird
}

type violation struct {
	File  string `json:"file"`
	Line  int    `json:"line"`
	Path  string `json:"import"`
	Alias string `json:"alias,omitempty"`
	Group string `json:"group"`
	After string `json:"after"`
}

// checkFile parses filePath and returns any import-order violations.
func checkFile(filePath string) ([]violation, error) {
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, filePath, nil, parser.ImportsOnly)
	if err != nil {
		return nil, err
	}

	currentModule := findModule(filePath)

	// Imports should already be in source order; sort by position to be safe.
	specs := make([]*ast.ImportSpec, len(f.Imports))
	copy(specs, f.Imports)
	sort.Slice(specs, func(i, j int) bool {
		return specs[i].Path.Pos() < specs[j].Path.Pos()
	})

	var violations []violation
	maxGroup := -1

	for _, spec := range specs {
		importPath := strings.Trim(spec.Path.Value, `"`)
		alias := ""
		if spec.Name != nil {
			alias = spec.Name.Name
		}

		group := classify(importPath, alias, currentModule)
		line := fset.Position(spec.Path.Pos()).Line

		if group < maxGroup {
			violations = append(violations, violation{
				File:  filePath,
				Line:  line,
				Path:  importPath,
				Alias: alias,
				Group: groupNames[group],
				After: groupNames[maxGroup],
			})
		} else {
			maxGroup = group
		}
	}

	return violations, nil
}

// collectGoFiles filters a newline-separated list of paths to existing .go files,
// deduplicating across multiple calls via the seen map.
func collectGoFiles(output string, seen map[string]bool) []string {
	var files []string
	for line := range strings.SplitSeq(output, "\n") {
		line = strings.TrimSpace(line)
		if !strings.HasSuffix(line, ".go") || seen[line] {
			continue
		}
		if _, err := os.Stat(line); err == nil {
			seen[line] = true
			files = append(files, line)
		}
	}
	return files
}

// findJJRoot walks parent directories of dir looking for a .jj/ directory and
// returns the workspace root path, or "" if none is found.
func findJJRoot(dir string) string {
	if !filepath.IsAbs(dir) {
		cwd, err := os.Getwd()
		if err != nil {
			return ""
		}
		dir = filepath.Join(cwd, dir)
	}
	for {
		if info, err := os.Stat(filepath.Join(dir, ".jj")); err == nil && info.IsDir() {
			return dir
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return ""
		}
		dir = parent
	}
}

// changedGoFiles returns .go files changed in the current jj change (preferred)
// or the current git diff, depending on which VCS is active.
func changedGoFiles() []string {
	if _, err := exec.LookPath("jj"); err == nil {
		if files, ok := jjChangedGoFiles(); ok {
			return files
		}
	}
	return gitChangedGoFiles()
}

// jjChangedGoFiles returns .go files in the current jj working-copy change.
// Returns (nil, false) when jj is not set up for this project or jj fails.
func jjChangedGoFiles() ([]string, bool) {
	cwd, err := os.Getwd()
	if err != nil {
		return nil, false
	}
	// Require a .jj/ directory in the project tree — jj being on PATH is not
	// sufficient; the project itself must be initialised as a jj workspace.
	if findJJRoot(cwd) == "" {
		return nil, false
	}
	// --name-only prints one path per line with no status prefix.
	out, err := exec.Command("jj", "diff", "--name-only").Output()
	if err != nil {
		return nil, false
	}
	seen := map[string]bool{}
	return collectGoFiles(string(out), seen), true
}

// gitChangedGoFiles returns .go files that appear in git diff HEAD or --cached.
func gitChangedGoFiles() []string {
	seen := map[string]bool{}
	var files []string
	for _, args := range [][]string{
		{"diff", "--name-only", "HEAD"},
		{"diff", "--name-only", "--cached"},
	} {
		out, err := exec.Command("git", args...).Output()
		if err != nil {
			continue
		}
		files = append(files, collectGoFiles(string(out), seen)...)
	}
	return files
}

func main() {
	// Collect file arguments, ignoring anything that starts with "-" (including
	// "--") so callers can use "go run go-import-checker.go -- a.go b.go"
	// without go run treating the listed .go files as additional source files.
	var files []string
	for _, arg := range os.Args[1:] {
		if strings.HasPrefix(arg, "-") {
			continue
		}
		files = append(files, arg)
	}

	if len(files) == 0 {
		files = changedGoFiles()
	}

	if len(files) == 0 {
		enc := json.NewEncoder(os.Stdout)
		enc.SetIndent("", "  ")
		_ = enc.Encode(struct {
			Checked    int         `json:"checked"`
			Violations []violation `json:"violations"`
		}{Violations: []violation{}})
		os.Exit(0)
	}

	type result struct {
		Checked    int         `json:"checked"`
		Violations []violation `json:"violations"`
		Doc        string      `json:"doc,omitempty"`
	}

	res := result{Violations: []violation{}}

	for _, f := range files {
		v, err := checkFile(f)
		if err != nil {
			fmt.Fprintf(os.Stderr, "parse error %s: %v\n", f, err)
			os.Exit(2)
		}
		res.Violations = append(res.Violations, v...)
		res.Checked++
	}

	if len(res.Violations) > 0 {
		res.Doc = "https://github.com/longhorn/longhorn/wiki/coding-convention#organize-package-imports"
	}

	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	_ = enc.Encode(res)

	if len(res.Violations) > 0 {
		os.Exit(1)
	}
}
