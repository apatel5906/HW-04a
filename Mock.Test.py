"""
Arpit Patel

"""
from githubAPI import get_repos, retrieve_commits
from unittest import mock
import unittest


class MockGitHubAPI(unittest.TestCase):

    @mock.patch('githubAPI.get_repos')
    def mock_get_repos_2(self, mock_repo_names):
        mock_repo_names.return_value = ['HW-04a', 'SSW--567', 'python-gedcom', 'HW-02b']

        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 4, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)



    @mock.patch('githubAPI.get_repos')
    def mock_invalid_user(self, mock_repo_name):
        mock_repo_name.return_value = []
        repos = get_repos('sdvnjnWfassvav')
        self.assertEqual(len(repos), 0, "Error: Invalid Username")


if __name__ == '__main__':
    print("Unit Test: Start")
    unittest.main()