
import os
from pathlib import Path

from ariadne import QueryType, load_schema_from_path
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema
import grpc
from protos.generated.svc_pb2 import HelloRequest, UserInfoRequest

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


@query.field("UserInfo")
def user_info(self, info, email):
    with grpc.insecure_channel('host.docker.internal:50052', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub = HelloWorldServiceStub(channel)
        response = stub.GetUserInfo(UserInfoRequest(email=email))
    return {
        "first_name": response.first_name,
        "last_name": response.last_name,
        "phone": response.phone,
        "country": response.country
    }


type_defs = load_schema_from_path(
    Path(Path(__file__).parent, "schema.graphql").__fspath__()
)


schema = make_federated_schema(type_defs, query)

app = GraphQL(schema)
