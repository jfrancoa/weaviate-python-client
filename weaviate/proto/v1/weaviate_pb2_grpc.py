# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from weaviate.proto.v1 import batch_pb2 as v1_dot_batch__pb2
from weaviate.proto.v1 import search_get_pb2 as v1_dot_search__get__pb2


class WeaviateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
            "/weaviate.v1.Weaviate/Search",
            request_serializer=v1_dot_search__get__pb2.SearchRequest.SerializeToString,
            response_deserializer=v1_dot_search__get__pb2.SearchReply.FromString,
        )
        self.BatchObjects = channel.unary_unary(
            "/weaviate.v1.Weaviate/BatchObjects",
            request_serializer=v1_dot_batch__pb2.BatchObjectsRequest.SerializeToString,
            response_deserializer=v1_dot_batch__pb2.BatchObjectsReply.FromString,
        )


class WeaviateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchObjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_WeaviateServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Search": grpc.unary_unary_rpc_method_handler(
            servicer.Search,
            request_deserializer=v1_dot_search__get__pb2.SearchRequest.FromString,
            response_serializer=v1_dot_search__get__pb2.SearchReply.SerializeToString,
        ),
        "BatchObjects": grpc.unary_unary_rpc_method_handler(
            servicer.BatchObjects,
            request_deserializer=v1_dot_batch__pb2.BatchObjectsRequest.FromString,
            response_serializer=v1_dot_batch__pb2.BatchObjectsReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "weaviate.v1.Weaviate", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Weaviate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Search(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/Search",
            v1_dot_search__get__pb2.SearchRequest.SerializeToString,
            v1_dot_search__get__pb2.SearchReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BatchObjects(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/weaviate.v1.Weaviate/BatchObjects",
            v1_dot_batch__pb2.BatchObjectsRequest.SerializeToString,
            v1_dot_batch__pb2.BatchObjectsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
