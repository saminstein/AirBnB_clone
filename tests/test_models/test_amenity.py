#!/usr/bin/python3

'''
This module defines the unittest case for the models/amenity.py
'''

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        ''' setup Amenity for instance to use for all test '''

        self.amenity = Amenity()

    def test_inits(self):
        ''' tests Amenity Initialization '''

        self.assertIsInstance(self.amenity, Amenity)

    def test_inherits(self):
        ''' tests if Amenity inherits from BaseModel '''
        self.assertIsInstance(self.amenity, BaseModel)

    def test_name(self):
        ''' tests if name is an attr of Amenity '''

        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name_value(self):
        ''' tests if name attr has the correct value '''
        self.assertEqual(self.amenity.name, '')
        self.amenity.name = 'Wifi'
        self.assertEqual(self.amenity.name, 'Wifi')


if '__name__' == '__main__':
    unittest.main()
