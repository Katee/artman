# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='googleapis.artman',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\x11googleapis.artman\"e\n\x06\x43onfig\x12+\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1b.googleapis.artman.Artifact\x12.\n\tartifacts\x18\x02 \x03(\x0b\x32\x1b.googleapis.artman.Artifact\"\x83\x0b\n\x08\x41rtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x61pi_name\x18\x02 \x01(\t\x12\x13\n\x0b\x61pi_version\x18\x03 \x01(\t\x12\x19\n\x11organization_name\x18\x04 \x01(\t\x12?\n\rrelease_level\x18\x05 \x01(\x0e\x32(.googleapis.artman.Artifact.ReleaseLevel\x12\x17\n\x0fsrc_proto_paths\x18\x06 \x03(\t\x12?\n\nproto_deps\x18\x07 \x03(\x0b\x32+.googleapis.artman.Artifact.ProtoDependency\x12\x44\n\x0ftest_proto_deps\x18\x08 \x03(\x0b\x32+.googleapis.artman.Artifact.ProtoDependency\x12\x14\n\x0cservice_yaml\x18\t \x01(\t\x12\x12\n\ngapic_yaml\x18\n \x01(\t\x12.\n\x04type\x18\x0c \x01(\x0e\x32 .googleapis.artman.Artifact.Type\x12\x36\n\x08language\x18\r \x01(\x0e\x32$.googleapis.artman.Artifact.Language\x12\x43\n\x0fpackage_version\x18\x0e \x01(\x0b\x32*.googleapis.artman.Artifact.PackageVersion\x12\x42\n\x0fpublish_targets\x18\x0f \x03(\x0b\x32).googleapis.artman.Artifact.PublishTarget\x12\x15\n\rdiscovery_doc\x18\x10 \x01(\t\x1a\x33\n\x0fProtoDependency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproto_path\x18\x02 \x01(\t\x1a]\n\x0ePackageVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1c\n\x14grpc_dep_lower_bound\x18\x02 \x01(\t\x12\x1c\n\x14grpc_dep_upper_bound\x18\x03 \x01(\t\x1a\xb7\x02\n\rPublishTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12<\n\x04type\x18\x03 \x01(\x0e\x32..googleapis.artman.Artifact.PublishTarget.Type\x12V\n\x12\x64irectory_mappings\x18\x04 \x03(\x0b\x32:.googleapis.artman.Artifact.PublishTarget.DirectoryMapping\x1a;\n\x10\x44irectoryMapping\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65st\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"3\n\x04Type\x12\x1f\n\x1bPUBLISHING_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06GITHUB\x10\x01\"J\n\x0cReleaseLevel\x12\x1d\n\x19RELEASE_LEVEL_UNSPECIFIED\x10\x00\x12\x06\n\x02GA\x10\x01\x12\x08\n\x04\x42\x45TA\x10\x02\x12\t\n\x05\x41LPHA\x10\x03\"r\n\x04Type\x12\t\n\x05GAPIC\x10\x00\x12\x10\n\x0cGAPIC_CONFIG\x10\x01\x12\x08\n\x04GRPC\x10\x02\x12\x0c\n\x08PROTOBUF\x10\x03\x12\x0e\n\nDISCOGAPIC\x10\x04\x12\x15\n\x11\x44ISCOGAPIC_CONFIG\x10\x05\x12\x0e\n\nGAPIC_ONLY\x10\x63\"m\n\x08Language\x12\x18\n\x14LANGUAGE_UNSPECIFIED\x10\x00\x12\x08\n\x04JAVA\x10\x01\x12\n\n\x06PYTHON\x10\x02\x12\n\n\x06NODEJS\x10\x03\x12\x06\n\x02GO\x10\x04\x12\x07\n\x03PHP\x10\x05\x12\n\n\x06\x43SHARP\x10\x06\x12\x08\n\x04RUBY\x10\x07J\x04\x08\x0b\x10\x0cR\x11import_proto_pathb\x06proto3')
)



_ARTIFACT_PUBLISHTARGET_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='googleapis.artman.Artifact.PublishTarget.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUBLISHING_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GITHUB', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1171,
  serialized_end=1222,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACT_PUBLISHTARGET_TYPE)

_ARTIFACT_RELEASELEVEL = _descriptor.EnumDescriptor(
  name='ReleaseLevel',
  full_name='googleapis.artman.Artifact.ReleaseLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RELEASE_LEVEL_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BETA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALPHA', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1224,
  serialized_end=1298,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACT_RELEASELEVEL)

_ARTIFACT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='googleapis.artman.Artifact.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GAPIC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAPIC_CONFIG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRPC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOGAPIC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOGAPIC_CONFIG', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAPIC_ONLY', index=6, number=99,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1300,
  serialized_end=1414,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACT_TYPE)

_ARTIFACT_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='googleapis.artman.Artifact.Language',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANGUAGE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PYTHON', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NODEJS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GO', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHP', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSHARP', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUBY', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1416,
  serialized_end=1525,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACT_LANGUAGE)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='googleapis.artman.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='googleapis.artman.Config.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifacts', full_name='googleapis.artman.Config.artifacts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=136,
)


_ARTIFACT_PROTODEPENDENCY = _descriptor.Descriptor(
  name='ProtoDependency',
  full_name='googleapis.artman.Artifact.ProtoDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='googleapis.artman.Artifact.ProtoDependency.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_path', full_name='googleapis.artman.Artifact.ProtoDependency.proto_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=762,
  serialized_end=813,
)

_ARTIFACT_PACKAGEVERSION = _descriptor.Descriptor(
  name='PackageVersion',
  full_name='googleapis.artman.Artifact.PackageVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='googleapis.artman.Artifact.PackageVersion.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpc_dep_lower_bound', full_name='googleapis.artman.Artifact.PackageVersion.grpc_dep_lower_bound', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpc_dep_upper_bound', full_name='googleapis.artman.Artifact.PackageVersion.grpc_dep_upper_bound', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=908,
)

_ARTIFACT_PUBLISHTARGET_DIRECTORYMAPPING = _descriptor.Descriptor(
  name='DirectoryMapping',
  full_name='googleapis.artman.Artifact.PublishTarget.DirectoryMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='googleapis.artman.Artifact.PublishTarget.DirectoryMapping.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest', full_name='googleapis.artman.Artifact.PublishTarget.DirectoryMapping.dest', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='googleapis.artman.Artifact.PublishTarget.DirectoryMapping.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1169,
)

_ARTIFACT_PUBLISHTARGET = _descriptor.Descriptor(
  name='PublishTarget',
  full_name='googleapis.artman.Artifact.PublishTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='googleapis.artman.Artifact.PublishTarget.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='googleapis.artman.Artifact.PublishTarget.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='googleapis.artman.Artifact.PublishTarget.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directory_mappings', full_name='googleapis.artman.Artifact.PublishTarget.directory_mappings', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARTIFACT_PUBLISHTARGET_DIRECTORYMAPPING, ],
  enum_types=[
    _ARTIFACT_PUBLISHTARGET_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=911,
  serialized_end=1222,
)

_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='googleapis.artman.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='googleapis.artman.Artifact.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_name', full_name='googleapis.artman.Artifact.api_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='googleapis.artman.Artifact.api_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_name', full_name='googleapis.artman.Artifact.organization_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_level', full_name='googleapis.artman.Artifact.release_level', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_proto_paths', full_name='googleapis.artman.Artifact.src_proto_paths', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_deps', full_name='googleapis.artman.Artifact.proto_deps', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_proto_deps', full_name='googleapis.artman.Artifact.test_proto_deps', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_yaml', full_name='googleapis.artman.Artifact.service_yaml', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gapic_yaml', full_name='googleapis.artman.Artifact.gapic_yaml', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='googleapis.artman.Artifact.type', index=10,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='googleapis.artman.Artifact.language', index=11,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_version', full_name='googleapis.artman.Artifact.package_version', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_targets', full_name='googleapis.artman.Artifact.publish_targets', index=13,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discovery_doc', full_name='googleapis.artman.Artifact.discovery_doc', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARTIFACT_PROTODEPENDENCY, _ARTIFACT_PACKAGEVERSION, _ARTIFACT_PUBLISHTARGET, ],
  enum_types=[
    _ARTIFACT_RELEASELEVEL,
    _ARTIFACT_TYPE,
    _ARTIFACT_LANGUAGE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=1550,
)

_CONFIG.fields_by_name['common'].message_type = _ARTIFACT
_CONFIG.fields_by_name['artifacts'].message_type = _ARTIFACT
_ARTIFACT_PROTODEPENDENCY.containing_type = _ARTIFACT
_ARTIFACT_PACKAGEVERSION.containing_type = _ARTIFACT
_ARTIFACT_PUBLISHTARGET_DIRECTORYMAPPING.containing_type = _ARTIFACT_PUBLISHTARGET
_ARTIFACT_PUBLISHTARGET.fields_by_name['type'].enum_type = _ARTIFACT_PUBLISHTARGET_TYPE
_ARTIFACT_PUBLISHTARGET.fields_by_name['directory_mappings'].message_type = _ARTIFACT_PUBLISHTARGET_DIRECTORYMAPPING
_ARTIFACT_PUBLISHTARGET.containing_type = _ARTIFACT
_ARTIFACT_PUBLISHTARGET_TYPE.containing_type = _ARTIFACT_PUBLISHTARGET
_ARTIFACT.fields_by_name['release_level'].enum_type = _ARTIFACT_RELEASELEVEL
_ARTIFACT.fields_by_name['proto_deps'].message_type = _ARTIFACT_PROTODEPENDENCY
_ARTIFACT.fields_by_name['test_proto_deps'].message_type = _ARTIFACT_PROTODEPENDENCY
_ARTIFACT.fields_by_name['type'].enum_type = _ARTIFACT_TYPE
_ARTIFACT.fields_by_name['language'].enum_type = _ARTIFACT_LANGUAGE
_ARTIFACT.fields_by_name['package_version'].message_type = _ARTIFACT_PACKAGEVERSION
_ARTIFACT.fields_by_name['publish_targets'].message_type = _ARTIFACT_PUBLISHTARGET
_ARTIFACT_RELEASELEVEL.containing_type = _ARTIFACT
_ARTIFACT_TYPE.containing_type = _ARTIFACT
_ARTIFACT_LANGUAGE.containing_type = _ARTIFACT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:googleapis.artman.Config)
  ))
_sym_db.RegisterMessage(Config)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), dict(

  ProtoDependency = _reflection.GeneratedProtocolMessageType('ProtoDependency', (_message.Message,), dict(
    DESCRIPTOR = _ARTIFACT_PROTODEPENDENCY,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:googleapis.artman.Artifact.ProtoDependency)
    ))
  ,

  PackageVersion = _reflection.GeneratedProtocolMessageType('PackageVersion', (_message.Message,), dict(
    DESCRIPTOR = _ARTIFACT_PACKAGEVERSION,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:googleapis.artman.Artifact.PackageVersion)
    ))
  ,

  PublishTarget = _reflection.GeneratedProtocolMessageType('PublishTarget', (_message.Message,), dict(

    DirectoryMapping = _reflection.GeneratedProtocolMessageType('DirectoryMapping', (_message.Message,), dict(
      DESCRIPTOR = _ARTIFACT_PUBLISHTARGET_DIRECTORYMAPPING,
      __module__ = 'config_pb2'
      # @@protoc_insertion_point(class_scope:googleapis.artman.Artifact.PublishTarget.DirectoryMapping)
      ))
    ,
    DESCRIPTOR = _ARTIFACT_PUBLISHTARGET,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:googleapis.artman.Artifact.PublishTarget)
    ))
  ,
  DESCRIPTOR = _ARTIFACT,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:googleapis.artman.Artifact)
  ))
_sym_db.RegisterMessage(Artifact)
_sym_db.RegisterMessage(Artifact.ProtoDependency)
_sym_db.RegisterMessage(Artifact.PackageVersion)
_sym_db.RegisterMessage(Artifact.PublishTarget)
_sym_db.RegisterMessage(Artifact.PublishTarget.DirectoryMapping)


# @@protoc_insertion_point(module_scope)
