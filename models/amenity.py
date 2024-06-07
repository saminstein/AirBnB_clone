#!/usr/bin/python3
'''
This module inherits from BaseModel, it contains
all the attributes to assign to amenities
'''
from models.base_model import BaseModel
import json


class Amenity(BaseModel):
    '''Amenity class

    attributes:
        name (str) - The name of the Amenity
    '''

    name = ''
