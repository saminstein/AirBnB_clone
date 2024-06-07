#!/usr/bin/python3
'''
This module inherits from BaseModel, it
contains all the attributes to assign to Review
'''
from models.base_model import BaseModel
import json


class Review(BaseModel):
    '''Review class

    attributes:
        place_id (str): The place id
        user_id (str): The user id
        text (str): The text review
    '''

    place_id = ''
    user_id = ''
    text = ''
