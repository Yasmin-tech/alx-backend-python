#!/usr/bin/env python3
""" Unittest classes for the class client.GithubOrgClient.
"""


from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class


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


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        An integration test for GithubOrgClient
        """

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        mock_get_json = cls.get_patcher.start()
        mock_response = MagicMock()
        mock_response.json.side_effect = [
                cls.org_payload[0],
                cls.repos_payload]
        mock_get_json.return_value = mock_response
        cls.obj = GithubOrgClient("google")

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ test GithubOrgClient.public_repos
            return the correct output
            """
        self.assertEqual(self.obj.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ test GithubOrgClient.public_repos with license
        returns the correct output
        """
        self.assertEqual(self.obj.public_repos(
            license="apache-2.0"),
            self.apache2_repos)
