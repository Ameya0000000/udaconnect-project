from marshmallow import Schema, fields
from flasgger import swag_from

from .models import Location
from .schemas import LocationSchema
from .services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from .grpcservice import GRPCService
from .kafkaservice import KafkaService

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

class MessageSchema(Schema):
    message = fields.Str(required=True)

@api.route("/api/")
class APIInfoResource(Resource):
    @swag_from('modules/location/swagger_configs/api_info.yml')  
    @responds(schema=MessageSchema)
    def get(self) -> dict:
        return {"message": "API is working"}, 200

@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):

    @swag_from('modules/location/swagger_configs/create_location.yml')  
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        location_data = request.get_json()
        location: Location = LocationService.create(location_data)

        # Send location via gRPC
        grpc_service = GRPCService(server_address="[::]:50051")
        grpc_response = grpc_service.send_location(location_data)

        return location

    @swag_from('modules/location/swagger_configs/get_location.yml')  
    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

def register_routes(api, app, root="api"):
    api.add_namespace(api)
