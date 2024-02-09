#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): City id.
        user_id (str): User id.
        name (str): The name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms of the.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): Maximum number of guests allowed.
        price_by_night (int): The price of the place by night.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity IDs.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
