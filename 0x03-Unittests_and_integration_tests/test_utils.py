#!/usr/bin/env python3
'''
    Unittese cases to set the functionality of the function
    <access_nested_map> in the utils model
    '''


import unittest
from unittest.mock import MagicMock, patch
from utils import access_nested_map
from utils import get_json
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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        '''
            Test that the access_nested_map function raises the correct
            Exception message
        '''
        with self.assertRaises(KeyError) as ex:
            access_nested_map(nested_map, path)
        self.assertEqual(str(ex.exception), "'{}'".format(exception))


class TestGetJson(unittest.TestCase):
    """
        Test cases for the function get_json
        """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """
        test that requests.get is called once with the given
        test_url parameter and return the correct output
        """
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_request_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)
        mock_request_get.assert_called_once_with(test_url)
