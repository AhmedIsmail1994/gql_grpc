
import os
from pathlib import Path

from ariadne import QueryType, load_schema_from_path
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema
import grpc
from protos.generated.svc_pb2 import HelloRequest

from protos.generated.svc_pb2_grpc import HelloWorldServiceStub

query = QueryType()

@query.field("HelloWorld")
def hello_world(self, info, input):
    with grpc.insecure_channel('host.docker.internal:50052', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub = HelloWorldServiceStub(channel)
        response = stub.SayHello(HelloRequest(name=input))    
    return {
        "message": response.message
    }

type_defs = load_schema_from_path(
    Path(Path(__file__).parent, "schema.graphql").__fspath__()
)


schema = make_federated_schema(type_defs, query)

app = GraphQL(schema)
    
    