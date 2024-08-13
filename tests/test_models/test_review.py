#!/usr/bin/python3

'''
This module defines the unittest for the models/review.py
'''

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        ''' sets review instance for all the tests '''

        self.review = Review()

    def test_inits(self):
        ''' tests review initialization '''

        self.assertIsInstance(self.review, Review)

    def test_inherit(self):
        ''' tests if review inherits from BaseModel class '''

        self.assertIsInstance(self.review, BaseModel)

    def test_place_id(self):
        ''' tests if place_id is an attr of Review & has the correct value '''

        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, '')
        self.review.place_id = 'uae023'
        self.assertEqual(self.review.place_id, 'uae023')

    def test_user_id(self):
        ''' tests if user_id is an attr of Review & has the correct value '''

        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, '')
        self.review.user_id = 'user77'
        self.assertEqual(self.review.user_id, 'user77')

    def test_text(self):
        ''' tests if text is an atrr of Review & has the correct value '''

        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, '')
        self.review.text = 'lovely'
        self.assertEqual(self.review.text, 'lovely')

    def test_to_dict_type(self):
        ''' tests if the to_dict type returns a dictionary '''

        self.assertIsInstance(self.review.to_dict(), dict)

    def test_to_dict_has_valid_keys(self):
        ''' tests if to_dict has the correct key '''

        self.assertIn('id', self.review.to_dict())
        self.assertIn('created_at', self.review.to_dict())
        self.assertIn('updated_at', self.review.to_dict())
        self.assertIn('__class__', self.review.to_dict())
