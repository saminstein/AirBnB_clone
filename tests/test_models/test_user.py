#!/usr/bin/python3
"""
This model defines the unittest case for the User clasd
"""

import unittest
import uuid
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        ''' setup method to initiliaze User object'''

        self.user = User()

    def test_init(self):
        ''' Tests user initialization '''

        self.assertIsInstance(self.user, User)

    def test_email_attr(self):
        ''' Tests if email is an attribute of user'''

        self.assertEqual(self.user.email, '')
        self.user.email = 'sam@alx.com'
        self.assertEqual(self.user.email, 'sam@alx.com')

    def test_password_attr(self):
        ''' Tests if password is an attribute of user '''

        self.assertEqual(self.user.password, '')
        self.user.password = 'df5&%'
        self.assertEqual(self.user.password, 'df5&%')

    def test_first_attr(self):
        ''' Tests if first_name is an attribute of user '''

        self.assertEqual(self.user.first_name, '')
        self.user.first_name = 'samuel'
        self.assertEqual(self.user.first_name, 'samuel')

    def test_last_attr(self):
        ''' Tests if last_name is an attribute of user '''

        self.assertEqual(self.user.last_name, '')
        self.user.last_name = 'shielu'
        self.assertEqual(self.user.last_name, 'shielu')

    def test_to_dict(self):
        ''' Tests if the to_dict returns a type dict '''

        self.assertIsInstance(User().to_dict(), dict)

    def test_to_dict_values(self):
        ''' Tests if to_dict contains correct keys '''

        dict_test = self.user.to_dict()

        self.assertIn('__class__', dict_test)
        self.assertEqual(dict_test['__class__'], 'User')

        self.assertIn('created_at', dict_test)
        self.assertEqual(dict_test['created_at'],
                         self.user.created_at.isoformat())

        self.assertIn('updated_at', dict_test)
        self.assertEqual(dict_test['updated_at'],
                         self.user.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
