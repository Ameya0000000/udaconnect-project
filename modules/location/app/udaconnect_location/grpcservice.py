import grpc
import location_pb2
import location_pb2_grpc

class GRPCService:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = location_pb2_grpc.LocationStub(self.channel)

    def send_message(self, message):
        request = location_pb2.LocationRequest(message=message)
        response = self.stub.Sendlocation(request)
        return response
