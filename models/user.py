#!/usr/bin/python3
'''
This module inherits from BaseModel and it
contains the attributes to assign to User
'''
from models.base_model import BaseModel
import json


class User(BaseModel):
    '''User Class

    attributes:
        email (str): email address of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
