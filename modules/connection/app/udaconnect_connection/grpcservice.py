import grpc
from . import connection_pb2
from . import connection_pb2_grpc

class GRPCService:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = connection_pb2_grpc.ConnectionStub(self.channel)

    def send_message(self, message):
        request = connection_pb2.ConnectionRequest(message=message)
        response = self.stub.SendConnection(request)
        return response
