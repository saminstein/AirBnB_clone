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

    def test_description(self):
        '''
        tests if description is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, '')
        self.place.description = 'Spacious'
        self.assertEqual(self.place.description, 'Spacious')

    def test_number_rooms(self):
        '''
        tests if number_rooms is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(self.place.number_rooms, 0)
        self.place.number_rooms = 36
        self.assertEqual(self.place.number_rooms, 36)

    def test_number_bathrooms(self):
        '''
        tests if number_bathrooms is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.place.number_bathrooms = 1
        self.assertEqual(self.place.number_bathrooms, 1)

    def test_max_guest(self):
        '''
        tests if max_guest is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)
        self.place.max_guest = 3
        self.assertEqual(self.place.max_guest, 3)

    def test_price_by_night(self):
        '''
        tests if price_by_night is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)
        self.place.price_by_night = 5
        self.assertEqual(self.place.price_by_night, 5)

    def test_latitude_attr(self):
        '''
        tests if latitude is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.price_by_night, 0.0)
        self.place.latitude = 2.82
        self.assertEqual(self.place.latitude, 2.82)

    def test_longitude_attr(self):
        '''
        tests if longitude is an attr of Place& has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)
        self.place.longitude = 3.42
        self.assertEqual(self.place.longitude, 3.42)

    def test_amenity_ids(self):
        '''
        tests if amenity_ids is an attr of Place & has the correct value
        '''

        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])
        self.place.amenity_ids = ['wifi', 'hot water']
        self.assertEqual(self.place.amenity_ids, ['wifi', 'hot water'])

if __name__ == "__main__":
    unittest.main()
