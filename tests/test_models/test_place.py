#!/usr/bin/python3

'''
This module defines all unittests cases for model/place.py
'''

import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        '''
        sets place instance for all the tests
        '''

        self.place = Place()

    def test_inits(self):
        '''
        tests place initialization 
        '''

        self.assertIsInstance(self.place, Place)

    def test_inherit(self):
        '''
        tests if place inherits from the BaseModel class
        '''

        self.assertIsInstance(self.place, BaseModel)

    def test_city_id(self):
        '''
        tests if city_id is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, '')
        self.place.city_id = 'ukr567'
        self.assertEqual(self.place.city_id, 'ukr567')

    def test_user_id(self):
        '''
        tests if user_id is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, '')
        self.place.user_id = 'sam007'
        self.assertEqual(self.place.user_id, 'sam007')

    def test_name(self):
        '''
        tests if name is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, '')
        self.place.name = 'London'
        self.assertEqual(self.place.name, 'London')
    
