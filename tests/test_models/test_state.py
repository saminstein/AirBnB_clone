#!/usr/bin/python3

"""
This model defines the unittest case for the models/state.py
"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        ''' setup State instance to use for all test '''

        self.state = State()

    def test_inits(self):
        ''' tests State initialization '''

        self.assertIsInstance(self.state, State)

    def test_inherits(self):
        ''' tests if Class inherits from BaseModel '''

        self.assertIsInstance(self.state, BaseModel)

    def test_name(self):
        ''' tests if name is an attr of State '''

        self.assertTrue(hasattr(self.state, 'name'))

    def test_name_value(self):
        ''' tests if name has the correct value '''

        self.assertEqual(self.state.name, '')
        self.state.name = "Edo"
        self.assertEqual(self.state.name, "Edo")

if '__name__' == '__main__':
    unittest.main()
