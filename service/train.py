from protobuf import train_pb2_grpc
from service.functions import train_funcions


class Train(train_pb2_grpc.TrainServicer):
    def Training(self, request, context):
        print("\n\tIncomming request to train data")
        return train_funcions.train(request.block)
