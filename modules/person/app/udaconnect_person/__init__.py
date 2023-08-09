from .models import Person  # noqa
from .schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from .controllers import api as person_api

    api.add_namespace(person_api, path=f"/{root}")
