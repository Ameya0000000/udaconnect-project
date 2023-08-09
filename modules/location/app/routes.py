from flask import Blueprint
from .udaconnect_location.controllers import api

def configure_routes(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

def register_routes(api, app, root="api"):
    from .udaconnect_location.controllers import register_routes as attach_location

    # Add routes
    attach_location(api, app)
