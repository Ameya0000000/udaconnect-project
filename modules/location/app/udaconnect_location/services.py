import logging
from datetime import datetime, timedelta
from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy
from .models import Location
from .schemas import LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from .kafkaservice import KafkaService

db = SQLAlchemy()

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location-api")

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.session.add(new_location)
        db.session.commit()

        kafka_service = KafkaService(kafka_topic="location_topic")
        kafka_service.send_message(str(new_location.id))

        return new_location
