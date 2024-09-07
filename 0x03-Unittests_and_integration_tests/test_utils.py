#!/usr/bin/env python3
'''
    Unittese cases to set the functionality of the function
    <access_nested_map> in the utils model
    '''


import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''
        unittest class to test the function access_nested_map
        '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        '''
         Test if access_nested_map return the correct output based on the
         parameterized inputs
         '''
        self.assertEqual(access_nested_map(nested_map, path), result)
