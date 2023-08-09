from .models import Location  # noqa
from .schemas import LocationSchema  # noqa


def register_routes(api, app, root="api"):
    from .controllers import api as location_api

    api.add_namespace(location_api, path=f"/{root}")
