# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gomoku.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'gomoku.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cgomoku.proto\"?\n\rJogadaRequest\x12\r\n\x05linha\x18\x01 \x01(\x05\x12\x0e\n\x06\x63oluna\x18\x02 \x01(\x05\x12\x0f\n\x07jogador\x18\x03 \x01(\t\"!\n\x0eJogadaResponse\x12\x0f\n\x07sucesso\x18\x01 \x01(\x08\"$\n\x10VencedorResponse\x12\x10\n\x08vencedor\x18\x01 \x01(\t\"#\n\x11TabuleiroResponse\x12\x0e\n\x06linhas\x18\x01 \x03(\t\"\x07\n\x05Vazio2\x8e\x01\n\x06Gomoku\x12(\n\x05Jogar\x12\x0e.JogadaRequest\x1a\x0f.JogadaResponse\x12.\n\x11VerificarVencedor\x12\x06.Vazio\x1a\x11.VencedorResponse\x12*\n\x0cGetTabuleiro\x12\x06.Vazio\x1a\x12.TabuleiroResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gomoku_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOGADAREQUEST']._serialized_start=16
  _globals['_JOGADAREQUEST']._serialized_end=79
  _globals['_JOGADARESPONSE']._serialized_start=81
  _globals['_JOGADARESPONSE']._serialized_end=114
  _globals['_VENCEDORRESPONSE']._serialized_start=116
  _globals['_VENCEDORRESPONSE']._serialized_end=152
  _globals['_TABULEIRORESPONSE']._serialized_start=154
  _globals['_TABULEIRORESPONSE']._serialized_end=189
  _globals['_VAZIO']._serialized_start=191
  _globals['_VAZIO']._serialized_end=198
  _globals['_GOMOKU']._serialized_start=201
  _globals['_GOMOKU']._serialized_end=343
# @@protoc_insertion_point(module_scope)
