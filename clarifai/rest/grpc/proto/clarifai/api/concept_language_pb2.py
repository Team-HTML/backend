# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/concept_language.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from clarifai.rest.grpc.proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2
from clarifai.rest.grpc.proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/concept_language.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n)proto/clarifai/api/concept_language.proto\x12\x0c\x63larifai.api\x1a\x1fproto/clarifai/api/common.proto\x1a&proto/clarifai/api/status/status.proto\x1a)proto/clarifai/api/utils/extensions.proto\"?\n\x0f\x43onceptLanguage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\"r\n\x19GetConceptLanguageRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x12\n\nconcept_id\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"\x82\x01\n\x1bListConceptLanguagesRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x12\n\nconcept_id\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\r\x12\x10\n\x08per_page\x18\x04 \x01(\r\"\xad\x01\n\x1cPatchConceptLanguagesRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x12\n\nconcept_id\x18\x02 \x01(\t\x12\x38\n\x11\x63oncept_languages\x18\x03 \x03(\x0b\x32\x1d.clarifai.api.ConceptLanguage\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\"\x9c\x01\n\x1bPostConceptLanguagesRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x12\n\nconcept_id\x18\x02 \x01(\t\x12\x38\n\x11\x63oncept_languages\x18\x03 \x03(\x0b\x32\x1d.clarifai.api.ConceptLanguage\"\x85\x01\n\x1dSingleConceptLanguageResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12\x37\n\x10\x63oncept_language\x18\x02 \x01(\x0b\x32\x1d.clarifai.api.ConceptLanguage\"\x8b\x01\n\x1cMultiConceptLanguageResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12>\n\x11\x63oncept_languages\x18\x02 \x03(\x0b\x32\x1d.clarifai.api.ConceptLanguageB\x04\x80\xb5\x18\x01\x42$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,])




_CONCEPTLANGUAGE = _descriptor.Descriptor(
  name='ConceptLanguage',
  full_name='clarifai.api.ConceptLanguage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.ConceptLanguage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='clarifai.api.ConceptLanguage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definition', full_name='clarifai.api.ConceptLanguage.definition', index=2,
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
  serialized_start=175,
  serialized_end=238,
)


_GETCONCEPTLANGUAGEREQUEST = _descriptor.Descriptor(
  name='GetConceptLanguageRequest',
  full_name='clarifai.api.GetConceptLanguageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetConceptLanguageRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.GetConceptLanguageRequest.concept_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='clarifai.api.GetConceptLanguageRequest.language', index=2,
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
  serialized_start=240,
  serialized_end=354,
)


_LISTCONCEPTLANGUAGESREQUEST = _descriptor.Descriptor(
  name='ListConceptLanguagesRequest',
  full_name='clarifai.api.ListConceptLanguagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.ListConceptLanguagesRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.ListConceptLanguagesRequest.concept_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='clarifai.api.ListConceptLanguagesRequest.page', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_page', full_name='clarifai.api.ListConceptLanguagesRequest.per_page', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=357,
  serialized_end=487,
)


_PATCHCONCEPTLANGUAGESREQUEST = _descriptor.Descriptor(
  name='PatchConceptLanguagesRequest',
  full_name='clarifai.api.PatchConceptLanguagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PatchConceptLanguagesRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.PatchConceptLanguagesRequest.concept_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_languages', full_name='clarifai.api.PatchConceptLanguagesRequest.concept_languages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='clarifai.api.PatchConceptLanguagesRequest.action', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=490,
  serialized_end=663,
)


_POSTCONCEPTLANGUAGESREQUEST = _descriptor.Descriptor(
  name='PostConceptLanguagesRequest',
  full_name='clarifai.api.PostConceptLanguagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostConceptLanguagesRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='clarifai.api.PostConceptLanguagesRequest.concept_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_languages', full_name='clarifai.api.PostConceptLanguagesRequest.concept_languages', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=666,
  serialized_end=822,
)


_SINGLECONCEPTLANGUAGERESPONSE = _descriptor.Descriptor(
  name='SingleConceptLanguageResponse',
  full_name='clarifai.api.SingleConceptLanguageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleConceptLanguageResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_language', full_name='clarifai.api.SingleConceptLanguageResponse.concept_language', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=825,
  serialized_end=958,
)


_MULTICONCEPTLANGUAGERESPONSE = _descriptor.Descriptor(
  name='MultiConceptLanguageResponse',
  full_name='clarifai.api.MultiConceptLanguageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiConceptLanguageResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_languages', full_name='clarifai.api.MultiConceptLanguageResponse.concept_languages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001')), file=DESCRIPTOR),
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
  serialized_start=961,
  serialized_end=1100,
)

_GETCONCEPTLANGUAGEREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_LISTCONCEPTLANGUAGESREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_PATCHCONCEPTLANGUAGESREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_PATCHCONCEPTLANGUAGESREQUEST.fields_by_name['concept_languages'].message_type = _CONCEPTLANGUAGE
_POSTCONCEPTLANGUAGESREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_POSTCONCEPTLANGUAGESREQUEST.fields_by_name['concept_languages'].message_type = _CONCEPTLANGUAGE
_SINGLECONCEPTLANGUAGERESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_SINGLECONCEPTLANGUAGERESPONSE.fields_by_name['concept_language'].message_type = _CONCEPTLANGUAGE
_MULTICONCEPTLANGUAGERESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTICONCEPTLANGUAGERESPONSE.fields_by_name['concept_languages'].message_type = _CONCEPTLANGUAGE
DESCRIPTOR.message_types_by_name['ConceptLanguage'] = _CONCEPTLANGUAGE
DESCRIPTOR.message_types_by_name['GetConceptLanguageRequest'] = _GETCONCEPTLANGUAGEREQUEST
DESCRIPTOR.message_types_by_name['ListConceptLanguagesRequest'] = _LISTCONCEPTLANGUAGESREQUEST
DESCRIPTOR.message_types_by_name['PatchConceptLanguagesRequest'] = _PATCHCONCEPTLANGUAGESREQUEST
DESCRIPTOR.message_types_by_name['PostConceptLanguagesRequest'] = _POSTCONCEPTLANGUAGESREQUEST
DESCRIPTOR.message_types_by_name['SingleConceptLanguageResponse'] = _SINGLECONCEPTLANGUAGERESPONSE
DESCRIPTOR.message_types_by_name['MultiConceptLanguageResponse'] = _MULTICONCEPTLANGUAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConceptLanguage = _reflection.GeneratedProtocolMessageType('ConceptLanguage', (_message.Message,), dict(
  DESCRIPTOR = _CONCEPTLANGUAGE,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ConceptLanguage)
  ))
_sym_db.RegisterMessage(ConceptLanguage)

GetConceptLanguageRequest = _reflection.GeneratedProtocolMessageType('GetConceptLanguageRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONCEPTLANGUAGEREQUEST,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetConceptLanguageRequest)
  ))
_sym_db.RegisterMessage(GetConceptLanguageRequest)

ListConceptLanguagesRequest = _reflection.GeneratedProtocolMessageType('ListConceptLanguagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONCEPTLANGUAGESREQUEST,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListConceptLanguagesRequest)
  ))
_sym_db.RegisterMessage(ListConceptLanguagesRequest)

PatchConceptLanguagesRequest = _reflection.GeneratedProtocolMessageType('PatchConceptLanguagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHCONCEPTLANGUAGESREQUEST,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PatchConceptLanguagesRequest)
  ))
_sym_db.RegisterMessage(PatchConceptLanguagesRequest)

PostConceptLanguagesRequest = _reflection.GeneratedProtocolMessageType('PostConceptLanguagesRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTCONCEPTLANGUAGESREQUEST,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostConceptLanguagesRequest)
  ))
_sym_db.RegisterMessage(PostConceptLanguagesRequest)

SingleConceptLanguageResponse = _reflection.GeneratedProtocolMessageType('SingleConceptLanguageResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLECONCEPTLANGUAGERESPONSE,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleConceptLanguageResponse)
  ))
_sym_db.RegisterMessage(SingleConceptLanguageResponse)

MultiConceptLanguageResponse = _reflection.GeneratedProtocolMessageType('MultiConceptLanguageResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTICONCEPTLANGUAGERESPONSE,
  __module__ = 'proto.clarifai.api.concept_language_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiConceptLanguageResponse)
  ))
_sym_db.RegisterMessage(MultiConceptLanguageResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
_MULTICONCEPTLANGUAGERESPONSE.fields_by_name['concept_languages'].has_options = True
_MULTICONCEPTLANGUAGERESPONSE.fields_by_name['concept_languages']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001'))
# @@protoc_insertion_point(module_scope)
