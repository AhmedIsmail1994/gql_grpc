from concurrent import futures
from abc import ABC, abstractmethod
from typing import List
import grpc
from grpc_reflection.v1alpha import reflection


class ServerInfo(ABC):
    @abstractmethod
    def add_to_server(self, server):
        raise NotImplementedError

    @abstractmethod
    def service_name(self):
        raise NotImplementedError


def setup_server(svcs: List[ServerInfo], port='[::]:50051', max_workers=10):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))

    service_names = []
    for svcr in svcs:
        svcr.add_to_server(server)
        service_names.append(svcr.service_name())

    service_names.append(reflection.SERVICE_NAME)
    reflection.enable_server_reflection(service_names, server)

    server.add_insecure_port(port)
    return server