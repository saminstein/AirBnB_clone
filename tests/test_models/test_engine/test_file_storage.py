#!/usr/bin/python3

"""
This module defines the unittest for models/engine/filestorage.py
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        '''
        sets up FileStorage object for each test
        '''

        self.storage = FileStorage()
        self.base = BaseModel()

    def test_instance(self):
        '''
        tests instance
        '''

        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        '''
        tests if all returns a dictionary
        '''

        self.assertIsInstance(self.storage.all(), dict)

    def test_save(self):
        '''
        tests if save method saves data correctly
        '''

        self.base.save()
        self.assertTrue(os.path.exists('./file.json'))
        os.remove('./file.json')

    def test_reload_w_args(self):
        '''
        test reload
        '''
        with self.assertRaises(TypeError):
            self.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
