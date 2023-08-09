import grpc
import person_pb2
import person_pb2_grpc

class GRPCService:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = person_pb2_grpc.PersonStub(self.channel)

    def send_message(self, message):
        request = person_pb2.PersonRequest(message=message)
        response = self.stub.SendPerson(request)
        return response
