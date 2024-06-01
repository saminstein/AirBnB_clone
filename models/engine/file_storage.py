#!/usr/bin/python3
'''
file storage module
'''

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State


class FileStorage:
    '''
    serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __filepath(str): path to the json file
        where the content will be stored
        __objects(dict): This will store all instance
        data
        class_dict(str): This is the dict of all
        the classes
    '''
    __file_path = 'file.json'
    __objects = {}

    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Amenity": Amenity,
            "City": City,
            "Review": Review,
            "State": State
            }

    def all(self):
        '''
        returns the dictionary __object
        '''
        return self.__objects

    def new(self, obj):
        '''
        adds an object to the __object dictionary
        attribute:
            obj: This is the object that you want
            to add to the  '__objects' dictionary
        '''
        class_name = obj.__class__.__name__
        object_id = obj.id
        key = class_name + '.' + object_id
        self.__objects[key] = obj

    def save(self):
        '''
        seralizes the dictionary to a json file
        '''
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        '''
        des6erializes the JSON file to __objects
        '''
        try:

            if path.exists(self.__file_path):
                with open(self.__file_path, mode='r', encoding='utf-8') as f:
                    json_dict = json.load(f)
                for k, v in json_dict.items():
                    obj = self.class_dict[v['__class__']](**v)
                    self.__objects[k] = obj
        except FileNotFoundError:
            pass
