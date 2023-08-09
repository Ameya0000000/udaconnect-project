from flask import Blueprint
from .udaconnect_connection.controllers import api

def configure_routes(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

def register_routes(api, app, root="api"):
    from .udaconnect_connection.controllers import register_routes as attach_connection

    # Add routes
    attach_connection(api, app)
