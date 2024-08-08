#!/usr/bin/python3

"""
This model defines the unittest case for the City class
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        ''' setup City instance to use for all test '''

        self.city = City()

    def test_inits(self):
        ''' tests City initialization '''

        self.assertIsInstance(self.city, City)

    def test_inherit(self):
        ''' tests if City inherits from BaseModel '''

        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_attr(self):
        ''' tests if state_id is an attribute of  city '''

        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_name_attr(self):
        ''' tests if name is an attribute of City '''

        self.assertTrue(hasattr(self.city, 'name'))

    def test_state_id_value(self):
        ''' tests if state_id attr has the correct value '''

        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "LA"
        self.assertEqual(self.city.state_id, "LA")

    def test_name_value(self):
        ''' tests if name attr has the correct value '''

        self.assertEqual(self.city.name, "")
        self.city.name = "Lagos"
        self.assertEqual(self.city.name, "Lagos")


if "__name__" == "__main__":
    unittest.main()
