#!/usr/bin/python3
'''
This module inherits from BaseModel, it contains
all the attributes to assign to place
'''
from models.base_model import BaseModel
import json


class Place(BaseModel):
    '''Place Class

    attributes:
        city_id (str): The id of the city
        user_id (str): The id of the user
        name (str): The name of the place
        description (str): The Place description
        number_rooms (int): The room numbers
        number_bathrooms (int): The bathroom numbers
        max_guest (int): The max number of guests
        price_by_night (int): The price per night of the Place
        latitude (float): The latitude of the Place
        longitude (float): The longitude of the Place
        amenity_ids (list): List contains all the amenities in the Place
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
