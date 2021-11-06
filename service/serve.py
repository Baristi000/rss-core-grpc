from protobuf import serve_pb2, serve_pb2_grpc
from service.functions import serve_functions


class Serve(serve_pb2_grpc.SearchServicer):
    def Search(self, request, context):
        print("\n\tIncomming request to search data")
        return serve_functions.search(request.message, request.result_number)
