from email import message

from protos.generated.svc_pb2_grpc import HelloWorldService, add_HelloWorldServiceServicer_to_server
from protos.generated.svc_pb2 import DESCRIPTOR, HelloResponse, UserInfoResponse


class HelloWorldSv(HelloWorldService):
    def add_to_server(self, server):
        add_HelloWorldServiceServicer_to_server(self, server)

    def service_name(self):
        return DESCRIPTOR.services_by_name["HelloWorldService"].full_name

    def SayHello(self, request, context):
        return HelloResponse(
            message=f'Hello World, ${request.name}'
        )

    def GetUserInfo(self, request, context):
        return UserInfoResponse(
            first_name="ahmed", last_name="ali", phone="+962234", country="EG"
        )
