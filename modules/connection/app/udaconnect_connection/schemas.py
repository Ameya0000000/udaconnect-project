from .models import Connection
from marshmallow import Schema, fields

class ConnectionSchema(Schema):
    location_id = fields.Integer()
    person_id = fields.Integer()
    creation_time = fields.DateTime()

    class Meta:
        model = Connection
