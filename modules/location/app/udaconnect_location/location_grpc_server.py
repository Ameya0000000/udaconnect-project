import grpc
from concurrent import futures
import location_pb2
import location_pb2_grpc

class LocationServiceServicer(location_pb2_grpc.LocationServiceServicer):
    def SendLocation(self, request, context):
        # Logging the received data for demonstration purposes
        response_message = f"Received location for Person ID: {request.person_id}. " \
                           f"Coordinates: ({request.latitude}, {request.longitude}) at {request.creation_time}."
        
        response = location_pb2.LocationResponse()
        response.message = response_message
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServiceServicer(), server)
    
    # Address and port here
    server_address = 'localhost:50051'
    server.add_insecure_port(server_address)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
