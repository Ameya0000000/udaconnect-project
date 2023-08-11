import grpc
from . import location_pb2
from . import location_pb2_grpc

class GRPCService:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = location_pb2_grpc.LocationStub(self.channel)

    def send_location(self, location):
        request = location_pb2.LocationRequest(
            person_id=location["person_id"],
            creation_time=location["creation_time"],
            latitude=location["latitude"],
            longitude=location["longitude"]
        )
        response = self.stub.SendLocation(request)
        return response.message
