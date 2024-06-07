#!/usr/bin/python3
'''
This is the module inherits from BaseModel and
contains attributes to assign to the states
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''State Class

    attributes:
        name (str): The name of the State
    '''
    name = ''
