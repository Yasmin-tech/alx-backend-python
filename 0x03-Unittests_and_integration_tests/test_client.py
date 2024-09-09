#!/usr/bin/env python3
""" Unittest classes for the class client.GithubOrgClient
"""


from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
            Test that GithubOrgClient._public_repos_url
            return the correct output
            """

        ORG_URL = "https://api.github.com/org/google"
        repos_url = "https://api.github.com/orgs/google/repos"

        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_org:
            obj = GithubOrgClient(ORG_URL)
            mock_org.return_value = {
                    "repos_url": "https://api.github.com/orgs/google/repos"
                    }
            self.assertEqual(obj._public_repos_url, repos_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
            Test that GithubOrgClient.public_repos
            returns the correct output
            """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [{
                "name": "truth",
                "full_name": "google/truth",
                "private": False},
                {
                "name": "new",
                "full_name": "google/truth",
                "private": True
                }]
        }
        mock_get_json.return_value = test_payload["repos"]

        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = test_payload["repos_url"]
            obj = GithubOrgClient("google")
            self.assertEqual(obj.public_repos(), ["truth", "new"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, license, license_key, result):
        """
            Test that GithubOrgClient.has_license
            returns the correct output
            """
        self.assertEqual(
                GithubOrgClient("test").has_license(license, license_key),
                result)
