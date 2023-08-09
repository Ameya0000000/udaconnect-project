from flask import request
from flasgger import swag_from
from flask_restx import Namespace, Resource
from .models import Person
from .services import PersonService
from .schemas import PersonSchema
from marshmallow import Schema, fields
from flask_accepts import responds

api = Namespace("UdaConnect", description="Person operations.") 

class MessageSchema(Schema):
    message = fields.Str(required=True)

@api.route("/api/")
class APIInfoResource(Resource):
    @responds(schema=MessageSchema)
    def get(self) -> dict:
        return {"message": "API is working"}, 200

@api.route("/persons")
class PersonResource(Resource):
    @swag_from('modules/person/swagger_configs/list_persons.yml')  
    def get(self):
        '''List all persons'''
        persons = PersonService.retrieve_all()
        return PersonSchema().dump(persons, many=True)

    @swag_from('modules/person/swagger_configs/create_person.yml')  
    def post(self):
        '''Create a new person'''
        new_person_data = request.get_json()
        new_person = PersonService.create(new_person_data)
        return PersonSchema().dump(new_person)

@api.route("/persons/<person_id>")
class PersonResourceById(Resource):
    @swag_from('modules/person/swagger_configs/get_person.yml')  
    def get(self, person_id):
        '''Get a person by ID'''
        person = PersonService.retrieve_by_id(person_id)
        return PersonSchema().dump(person)

def register_routes(api, app, root="api"):
    api.add_namespace(api)
