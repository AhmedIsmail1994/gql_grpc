from concurrent import futures

# from protos.generated.svc_pb2_grpc import HelloWorldServicer, add_HelloWorldServicer_to_server
from svc.hello_world_sv import HelloWorldSv
from svc.setup_server import setup_server


class Server:

    @staticmethod
    def run():
        server = setup_server([HelloWorldSv()])
        server.start()
        server.wait_for_termination()


if __name__ == "__main__":
    Server.run()
