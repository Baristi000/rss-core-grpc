from concurrent import futures
import grpc
import time
import threading
import sys

from protobuf import serve_pb2_grpc, train_pb2_grpc
from service.serve import Serve
from service.train import Train
from setting import settings


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(
        max_workers=settings.max_workers))

    train_pb2_grpc.add_TrainServicer_to_server(
        servicer=Train(), server=server)
    serve_pb2_grpc.add_SearchServicer_to_server(
        servicer=Serve(), server=server)

    server.add_insecure_port(settings.host)
    server.start()
    print("\tServer start completed")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("\nserver stop")
        server.stop(0)


if __name__ == "__main__":
    serve()
