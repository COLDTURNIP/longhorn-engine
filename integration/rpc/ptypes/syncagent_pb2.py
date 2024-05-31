# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ptypes/syncagent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ptypes import common_pb2 as ptypes_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ptypes/syncagent.proto\x12\x06ptypes\x1a\x1bgoogle/protobuf/empty.proto\x1a\x13ptypes/common.proto\"&\n\x11\x46ileRemoveRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"A\n\x11\x46ileRenameRequest\x12\x15\n\rold_file_name\x18\x01 \x01(\t\x12\x15\n\rnew_file_name\x18\x02 \x01(\t\"-\n\x15ReceiverLaunchRequest\x12\x14\n\x0cto_file_name\x18\x01 \x01(\t\"&\n\x16ReceiverLaunchResponse\x12\x0c\n\x04port\x18\x01 \x01(\x05\"\x7f\n\x0f\x46ileSendRequest\x12\x16\n\x0e\x66rom_file_name\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x11\n\tfast_sync\x18\x04 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x05 \x01(\x05\"\xa6\x01\n\x10\x46ilesSyncRequest\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x0f\n\x07to_host\x18\x02 \x01(\t\x12\x31\n\x13sync_file_info_list\x18\x03 \x03(\x0b\x32\x14.ptypes.SyncFileInfo\x12\x11\n\tfast_sync\x18\x04 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x05 \x01(\x05\"\xc1\x01\n\x14SnapshotCloneRequest\x12\x14\n\x0c\x66rom_address\x18\x01 \x01(\t\x12\x0f\n\x07to_host\x18\x02 \x01(\t\x12\x1a\n\x12snapshot_file_name\x18\x03 \x01(\t\x12%\n\x1d\x65xport_backing_image_if_exist\x18\x04 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x05 \x01(\x05\x12\x18\n\x10\x66rom_volume_name\x18\x06 \x01(\t\"\x9b\x01\n\x13VolumeExportRequest\x12\x1a\n\x12snapshot_file_name\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12%\n\x1d\x65xport_backing_image_if_exist\x18\x04 \x01(\x08\x12%\n\x1d\x66ile_sync_http_client_timeout\x18\x05 \x01(\x05\"\xf8\x03\n\x13\x42\x61\x63kupCreateRequest\x12\x1a\n\x12snapshot_file_name\x18\x01 \x01(\t\x12\x15\n\rbackup_target\x18\x02 \x01(\t\x12\x13\n\x0bvolume_name\x18\x03 \x01(\t\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12?\n\ncredential\x18\x05 \x03(\x0b\x32+.ptypes.BackupCreateRequest.CredentialEntry\x12\x1a\n\x12\x62\x61\x63king_image_name\x18\x06 \x01(\t\x12\x1e\n\x16\x62\x61\x63king_image_checksum\x18\x07 \x01(\t\x12\x13\n\x0b\x62\x61\x63kup_name\x18\x08 \x01(\t\x12\x1a\n\x12\x63ompression_method\x18\t \x01(\t\x12\x18\n\x10\x63oncurrent_limit\x18\n \x01(\x05\x12\x1a\n\x12storage_class_name\x18\x0b \x01(\t\x12?\n\nparameters\x18\x0c \x03(\x0b\x32+.ptypes.BackupCreateRequest.ParametersEntry\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\">\n\x14\x42\x61\x63kupCreateResponse\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\x12\x16\n\x0eis_incremental\x18\x02 \x01(\x08\"%\n\x13\x42\x61\x63kupRemoveRequest\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\"%\n\x13\x42\x61\x63kupStatusRequest\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\"q\n\x14\x42\x61\x63kupStatusResponse\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x12\n\nbackup_url\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x15\n\rsnapshot_name\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\"\xd1\x01\n\x14\x42\x61\x63kupRestoreRequest\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\x12\x1a\n\x12snapshot_disk_name\x18\x02 \x01(\t\x12@\n\ncredential\x18\x03 \x03(\x0b\x32,.ptypes.BackupRestoreRequest.CredentialEntry\x12\x18\n\x10\x63oncurrent_limit\x18\x04 \x01(\x05\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa7\x02\n!BackupRestoreIncrementallyRequest\x12\x0e\n\x06\x62\x61\x63kup\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65lta_file_name\x18\x02 \x01(\t\x12!\n\x19last_restored_backup_name\x18\x03 \x01(\t\x12\x1a\n\x12snapshot_disk_name\x18\x04 \x01(\t\x12M\n\ncredential\x18\x05 \x03(\x0b\x32\x39.ptypes.BackupRestoreIncrementallyRequest.CredentialEntry\x12\x18\n\x10\x63oncurrent_limit\x18\x06 \x01(\x05\x1a\x31\n\x0f\x43redentialEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc2\x01\n\x15RestoreStatusResponse\x12\x14\n\x0cis_restoring\x18\x01 \x01(\x08\x12\x15\n\rlast_restored\x18\x02 \x01(\t\x12\x10\n\x08progress\x18\x03 \x01(\x05\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65st_file_name\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x12\n\nbackup_url\x18\x07 \x01(\t\x12 \n\x18\x63urrent_restoring_backup\x18\x08 \x01(\t\"a\n\x1bSnapshotPurgeStatusResponse\x12\x12\n\nis_purging\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x10\n\x08progress\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\t\"\x83\x01\n\x1cReplicaRebuildStatusResponse\x12\x15\n\ris_rebuilding\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x10\n\x08progress\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\t\x12\x1c\n\x14\x66rom_replica_address\x18\x05 \x01(\t\"\x96\x01\n\x1bSnapshotCloneStatusResponse\x12\x12\n\nis_cloning\x18\x01 \x01(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x10\n\x08progress\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\t\x12\x1c\n\x14\x66rom_replica_address\x18\x05 \x01(\t\x12\x15\n\rsnapshot_name\x18\x06 \x01(\t\"<\n\x13SnapshotHashRequest\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\x12\x0e\n\x06rehash\x18\x02 \x01(\x08\"2\n\x19SnapshotHashStatusRequest\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\"h\n\x1aSnapshotHashStatusResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1a\n\x12silently_corrupted\x18\x04 \x01(\x08\"2\n\x19SnapshotHashCancelRequest\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\"2\n\x1dSnapshotHashLockStateResponse\x12\x11\n\tis_locked\x18\x01 \x01(\x08\x32\xc4\x0c\n\x10SyncAgentService\x12\x41\n\nFileRemove\x12\x19.ptypes.FileRemoveRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\nFileRename\x12\x19.ptypes.FileRenameRequest\x1a\x16.google.protobuf.Empty\"\x00\x12=\n\x08\x46ileSend\x12\x17.ptypes.FileSendRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\tFilesSync\x12\x18.ptypes.FilesSyncRequest\x1a\x16.google.protobuf.Empty\"\x00\x12G\n\rSnapshotClone\x12\x1c.ptypes.SnapshotCloneRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x45\n\x0cVolumeExport\x12\x1b.ptypes.VolumeExportRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Q\n\x0eReceiverLaunch\x12\x1d.ptypes.ReceiverLaunchRequest\x1a\x1e.ptypes.ReceiverLaunchResponse\"\x00\x12K\n\x0c\x42\x61\x63kupCreate\x12\x1b.ptypes.BackupCreateRequest\x1a\x1c.ptypes.BackupCreateResponse\"\x00\x12\x45\n\x0c\x42\x61\x63kupRemove\x12\x1b.ptypes.BackupRemoveRequest\x1a\x16.google.protobuf.Empty\"\x00\x12G\n\rBackupRestore\x12\x1c.ptypes.BackupRestoreRequest\x1a\x16.google.protobuf.Empty\"\x00\x12K\n\x0c\x42\x61\x63kupStatus\x12\x1b.ptypes.BackupStatusRequest\x1a\x1c.ptypes.BackupStatusResponse\"\x00\x12\x39\n\x05Reset\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\rRestoreStatus\x12\x16.google.protobuf.Empty\x1a\x1d.ptypes.RestoreStatusResponse\"\x00\x12\x41\n\rSnapshotPurge\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12T\n\x13SnapshotPurgeStatus\x12\x16.google.protobuf.Empty\x1a#.ptypes.SnapshotPurgeStatusResponse\"\x00\x12V\n\x14ReplicaRebuildStatus\x12\x16.google.protobuf.Empty\x1a$.ptypes.ReplicaRebuildStatusResponse\"\x00\x12T\n\x13SnapshotCloneStatus\x12\x16.google.protobuf.Empty\x1a#.ptypes.SnapshotCloneStatusResponse\"\x00\x12\x45\n\x0cSnapshotHash\x12\x1b.ptypes.SnapshotHashRequest\x1a\x16.google.protobuf.Empty\"\x00\x12]\n\x12SnapshotHashStatus\x12!.ptypes.SnapshotHashStatusRequest\x1a\".ptypes.SnapshotHashStatusResponse\"\x00\x12Q\n\x12SnapshotHashCancel\x12!.ptypes.SnapshotHashCancelRequest\x1a\x16.google.protobuf.Empty\"\x00\x12X\n\x15SnapshotHashLockState\x12\x16.google.protobuf.Empty\x1a%.ptypes.SnapshotHashLockStateResponse\"\x00\x42\x33Z1github.com/longhorn/types/pkg/generated/enginerpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ptypes.syncagent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/longhorn/types/pkg/generated/enginerpc'
  _BACKUPCREATEREQUEST_CREDENTIALENTRY._options = None
  _BACKUPCREATEREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _BACKUPCREATEREQUEST_PARAMETERSENTRY._options = None
  _BACKUPCREATEREQUEST_PARAMETERSENTRY._serialized_options = b'8\001'
  _BACKUPRESTOREREQUEST_CREDENTIALENTRY._options = None
  _BACKUPRESTOREREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _BACKUPRESTOREINCREMENTALLYREQUEST_CREDENTIALENTRY._options = None
  _BACKUPRESTOREINCREMENTALLYREQUEST_CREDENTIALENTRY._serialized_options = b'8\001'
  _globals['_FILEREMOVEREQUEST']._serialized_start=84
  _globals['_FILEREMOVEREQUEST']._serialized_end=122
  _globals['_FILERENAMEREQUEST']._serialized_start=124
  _globals['_FILERENAMEREQUEST']._serialized_end=189
  _globals['_RECEIVERLAUNCHREQUEST']._serialized_start=191
  _globals['_RECEIVERLAUNCHREQUEST']._serialized_end=236
  _globals['_RECEIVERLAUNCHRESPONSE']._serialized_start=238
  _globals['_RECEIVERLAUNCHRESPONSE']._serialized_end=276
  _globals['_FILESENDREQUEST']._serialized_start=278
  _globals['_FILESENDREQUEST']._serialized_end=405
  _globals['_FILESSYNCREQUEST']._serialized_start=408
  _globals['_FILESSYNCREQUEST']._serialized_end=574
  _globals['_SNAPSHOTCLONEREQUEST']._serialized_start=577
  _globals['_SNAPSHOTCLONEREQUEST']._serialized_end=770
  _globals['_VOLUMEEXPORTREQUEST']._serialized_start=773
  _globals['_VOLUMEEXPORTREQUEST']._serialized_end=928
  _globals['_BACKUPCREATEREQUEST']._serialized_start=931
  _globals['_BACKUPCREATEREQUEST']._serialized_end=1435
  _globals['_BACKUPCREATEREQUEST_CREDENTIALENTRY']._serialized_start=1335
  _globals['_BACKUPCREATEREQUEST_CREDENTIALENTRY']._serialized_end=1384
  _globals['_BACKUPCREATEREQUEST_PARAMETERSENTRY']._serialized_start=1386
  _globals['_BACKUPCREATEREQUEST_PARAMETERSENTRY']._serialized_end=1435
  _globals['_BACKUPCREATERESPONSE']._serialized_start=1437
  _globals['_BACKUPCREATERESPONSE']._serialized_end=1499
  _globals['_BACKUPREMOVEREQUEST']._serialized_start=1501
  _globals['_BACKUPREMOVEREQUEST']._serialized_end=1538
  _globals['_BACKUPSTATUSREQUEST']._serialized_start=1540
  _globals['_BACKUPSTATUSREQUEST']._serialized_end=1577
  _globals['_BACKUPSTATUSRESPONSE']._serialized_start=1579
  _globals['_BACKUPSTATUSRESPONSE']._serialized_end=1692
  _globals['_BACKUPRESTOREREQUEST']._serialized_start=1695
  _globals['_BACKUPRESTOREREQUEST']._serialized_end=1904
  _globals['_BACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_start=1335
  _globals['_BACKUPRESTOREREQUEST_CREDENTIALENTRY']._serialized_end=1384
  _globals['_BACKUPRESTOREINCREMENTALLYREQUEST']._serialized_start=1907
  _globals['_BACKUPRESTOREINCREMENTALLYREQUEST']._serialized_end=2202
  _globals['_BACKUPRESTOREINCREMENTALLYREQUEST_CREDENTIALENTRY']._serialized_start=1335
  _globals['_BACKUPRESTOREINCREMENTALLYREQUEST_CREDENTIALENTRY']._serialized_end=1384
  _globals['_RESTORESTATUSRESPONSE']._serialized_start=2205
  _globals['_RESTORESTATUSRESPONSE']._serialized_end=2399
  _globals['_SNAPSHOTPURGESTATUSRESPONSE']._serialized_start=2401
  _globals['_SNAPSHOTPURGESTATUSRESPONSE']._serialized_end=2498
  _globals['_REPLICAREBUILDSTATUSRESPONSE']._serialized_start=2501
  _globals['_REPLICAREBUILDSTATUSRESPONSE']._serialized_end=2632
  _globals['_SNAPSHOTCLONESTATUSRESPONSE']._serialized_start=2635
  _globals['_SNAPSHOTCLONESTATUSRESPONSE']._serialized_end=2785
  _globals['_SNAPSHOTHASHREQUEST']._serialized_start=2787
  _globals['_SNAPSHOTHASHREQUEST']._serialized_end=2847
  _globals['_SNAPSHOTHASHSTATUSREQUEST']._serialized_start=2849
  _globals['_SNAPSHOTHASHSTATUSREQUEST']._serialized_end=2899
  _globals['_SNAPSHOTHASHSTATUSRESPONSE']._serialized_start=2901
  _globals['_SNAPSHOTHASHSTATUSRESPONSE']._serialized_end=3005
  _globals['_SNAPSHOTHASHCANCELREQUEST']._serialized_start=3007
  _globals['_SNAPSHOTHASHCANCELREQUEST']._serialized_end=3057
  _globals['_SNAPSHOTHASHLOCKSTATERESPONSE']._serialized_start=3059
  _globals['_SNAPSHOTHASHLOCKSTATERESPONSE']._serialized_end=3109
  _globals['_SYNCAGENTSERVICE']._serialized_start=3112
  _globals['_SYNCAGENTSERVICE']._serialized_end=4716
# @@protoc_insertion_point(module_scope)
