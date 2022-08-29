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
            message=f'Hello World, {request.name}'
        )

    def GetUserInfo(self, request, context):
        users = [{
            "email": "hossam@nutrien.com",
            "first_name": "hossam",
            "last_name": "hassan",
            "country": "EG",
            "phone": "01010101010"
        }, {
            "email": "amir@nutrien.com",
            "first_name": "amir",
            "last_name": "ghanem",
            "country": "EG",
            "phone": "011011011011"
        }, {
            "email": "ahmed@nutrien.com",
            "first_name": "ahmed",
            "last_name": "ismail",
            "country": "EG",
            "phone": "015015015015"
        }, {
            "email": "test@nutrien.com",
            "first_name": "test",
            "last_name": "test",
            "country": "US",
            "phone": "+13324558954"
        }]
        user = [x for x in users if x['email'] == request.email][0]
        return UserInfoResponse(
            first_name=user['first_name'], last_name=user['last_name'], phone=user['phone'], country=user['country']
        )
