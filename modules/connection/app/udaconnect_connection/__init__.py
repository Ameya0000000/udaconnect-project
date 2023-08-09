from .models import Connection  # noqa
from .schemas import ConnectionSchema  # noqa


def register_routes(api, app, root="api"):
    from .controllers import api as connection_api

    api.add_namespace(connection_api, path=f"/{root}")
