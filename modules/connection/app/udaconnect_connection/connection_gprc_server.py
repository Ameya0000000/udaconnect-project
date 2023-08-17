import grpc
from concurrent import futures
import connection_pb2
import connection_pb2_grpc

class ConnectionServiceServicer(connection_pb2_grpc.ConnectionServiceServicer):
    def SendConnection(self, request, context):
       
        response = connection_pb2.ConnectionResponse()
        response.message = "Received message: " + request.message
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServiceServicer(), server)
    
    # Use the appropriate address and port here
    server_address = 'localhost:50051'
    server.add_insecure_port(server_address)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
