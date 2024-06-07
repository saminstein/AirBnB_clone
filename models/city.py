#!/usr/bin/python3
'''
This module inherits from 'BaseModel' and it
contains attributes assigned to the cities
'''
from models.base_model import BaseModel
import json


class City(BaseModel):
    '''City Class

    attributes:
        state_id (str): The id of the state
        name: The name of the city
    '''

    state_id = ''
    name = ''
