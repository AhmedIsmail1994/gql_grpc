from email import message

from svc_pb2_grpc import HelloWorldServicer, add_HelloWorldServicer_to_server
from svc_pb2 import HelloResponse


class HelloWorldSv(HelloWorldServicer):
    def add_to_server(self, server):
        add_HelloWorldServicer_to_server(self, server)
        
    def SayHello(self, request, context):
        return HelloResponse({
            message: f'Hello World, ${request.name}'
        })