# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import gomoku_pb2 as gomoku__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in gomoku_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GomokuStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Jogar = channel.unary_unary(
                '/Gomoku/Jogar',
                request_serializer=gomoku__pb2.JogadaRequest.SerializeToString,
                response_deserializer=gomoku__pb2.JogadaResponse.FromString,
                _registered_method=True)
        self.VerificarVencedor = channel.unary_unary(
                '/Gomoku/VerificarVencedor',
                request_serializer=gomoku__pb2.Vazio.SerializeToString,
                response_deserializer=gomoku__pb2.VencedorResponse.FromString,
                _registered_method=True)
        self.GetTabuleiro = channel.unary_unary(
                '/Gomoku/GetTabuleiro',
                request_serializer=gomoku__pb2.Vazio.SerializeToString,
                response_deserializer=gomoku__pb2.TabuleiroResponse.FromString,
                _registered_method=True)


class GomokuServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Jogar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerificarVencedor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTabuleiro(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GomokuServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Jogar': grpc.unary_unary_rpc_method_handler(
                    servicer.Jogar,
                    request_deserializer=gomoku__pb2.JogadaRequest.FromString,
                    response_serializer=gomoku__pb2.JogadaResponse.SerializeToString,
            ),
            'VerificarVencedor': grpc.unary_unary_rpc_method_handler(
                    servicer.VerificarVencedor,
                    request_deserializer=gomoku__pb2.Vazio.FromString,
                    response_serializer=gomoku__pb2.VencedorResponse.SerializeToString,
            ),
            'GetTabuleiro': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTabuleiro,
                    request_deserializer=gomoku__pb2.Vazio.FromString,
                    response_serializer=gomoku__pb2.TabuleiroResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Gomoku', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Gomoku', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Gomoku(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Jogar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Gomoku/Jogar',
            gomoku__pb2.JogadaRequest.SerializeToString,
            gomoku__pb2.JogadaResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerificarVencedor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Gomoku/VerificarVencedor',
            gomoku__pb2.Vazio.SerializeToString,
            gomoku__pb2.VencedorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTabuleiro(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Gomoku/GetTabuleiro',
            gomoku__pb2.Vazio.SerializeToString,
            gomoku__pb2.TabuleiroResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
