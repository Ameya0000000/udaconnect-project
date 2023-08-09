from typing import Dict, List

import logging
from datetime import datetime, timedelta
from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy
from .models import Connection
from .schemas import ConnectionSchema
from sqlalchemy.sql import text

db = SQLAlchemy()

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("connection-api")


class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ) -> List[Connection]:
        # Logic for find_contacts has to be modified as the connection microservice
        # does not have access to location and person data directly. You may need to use
        # API calls to Location and Person microservices to achieve this.
        pass
