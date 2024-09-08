#!/usr/bin/env python3
""" Unittest classes for the class client.GithubOrgClient
"""


from client import GithubOrgClient
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test the class TestGithubOrgClient
    """

    @parameterized.expand([
        ("google", {"login": "google", "id": 1342004}),
        ("abc", {"message": "Not Found"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, payload, mock_get_json):
        """
         Test that GithubOrgClient.org returns the correct value.
         Use @patch as a decorator to make sure get_json is
         called once with the expected argument
         """
        ORG_URL = "https://api.github.com/orgs/{}".format(org_name)
        obj = GithubOrgClient(org_name)
        mock_get_json.return_value = payload
        self.assertEqual(obj.org, payload)
        mock_get_json.assert_called_once_with(ORG_URL)
