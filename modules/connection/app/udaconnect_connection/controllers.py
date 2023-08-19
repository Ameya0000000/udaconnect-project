from datetime import datetime
from flasgger import swag_from
from marshmallow import Schema, fields as ma_fields
from .models import Connection
from .schemas import ConnectionSchema
from .services import ConnectionService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource, Api, fields

# Kafka Importation
from .kafkaservice import KafkaService

kafka_service = KafkaService(kafka_topic="connection_topic")

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")
api = Api(version='1.0', title='Connection API', description='A simple Connection API',)

ns = api.namespace('connections', description='Connection operations')

connection = api.model('Connection', {
    'id': fields.String(required=True, description='The connection identifier'),
    'name': fields.String(required=True, description='The connection details'),
})

class MessageSchema(Schema):
    message = ma_fields.Str(required=True)

@ns.route('/')
class ConnectionList(Resource):
    @swag_from('modules/connection/swagger_configs/list_connections.yml')  
    @ns.doc('list_connections')
    def get(self):
        '''List all connections'''
        pass

    @swag_from('modules/connection/swagger_configs/create_connection.yml')  
    @ns.doc('create_connection')
    @ns.expect(connection)
    def post(self):
        '''Create a new connection'''
        pass

@api.route("/api/")
class APIInfoResource(Resource):
    @responds(schema=MessageSchema)
    def get(self) -> dict:
        return {"message": "API is working"}, 200

@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Lower bound of date range", _in="query")
@api.param("end_date", "Upper bound of date range", _in="query")
@api.param("distance", "Proximity to a given user in meters", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        # Logic
        pass

def register_routes(api, app, root="api"):
    api.add_namespace(api)
