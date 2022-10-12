"""
Arpit Patel 


"""
from githubAPI import get_repos, retrieve_commits
from unittest import mock
import unittest


class MockGitAPI(unittest.TestCase):

    @mock.patch('GitApi.get_repos')
    def mock_get_repos_1(self, mock_repo_names):
        mock_repo_names.return_value = ['apatel5906','exp1-learning','SSW--567','HW-02b' , 'HW-04a']

        repos = get_repos('apatel5906')
        self.assertGreaterEqual(len(repos), 5, "User 'apatel5906' has 5 repositories")
        self.assertIn('apatel5906', repos)
        self.assertIn('SSW--567', repos)
        self.assertIn('HW-04a', repos)
        self.assertIn('HW-02b', repos)
        self.assertIn('exp1-learning', repos)

    @mock.patch('GitApi.get_repos')
    def mock_get_repos_2(self, mock_repo_names):
        mock_repo_names.return_value = ['apatel5906','exp1-learning','SSW--567','HW-02b' , 'HW-04a']

        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 4, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)

    @mock.patch('githubAPI.retrieve_commits')
    def mock_retrieve_commits(self, mock_repo_commits):
        mock_repo_commits.return_value = 2
        self.assertGreaterEqual(retrieve_commits('apatel5906', 'apatel5906'), 2)
        mock_repo_commits.return_value = 1
        self.assertGreaterEqual(retrieve_commits('apatel5906', 'exp1-learning'), 1)
        mock_repo_commits.return_value = 14
        self.assertGreaterEqual(retrieve_commits('apatel5906', 'HW-02b'), 14)
        mock_repo_commits.return_value = 5
        self.assertGreaterEqual(retrieve_commits('apatel5906', 'HW-04a'), 13)
        mock_repo_commits.return_value = 19
        self.assertGreaterEqual(retrieve_commits('apatel5906', 'SSW--567'), 1)

    @mock.patch('githubAPI.get_repos')
    def mock_invalid_user(self, mock_repo_name):
        mock_repo_name.return_value = []
        repos = get_repos('sdvnjnWfassvav')
        self.assertEqual(len(repos), 0, "Error: Invalid Username")


if __name__ == '__main__':
    print("Unit Test: Start")
    unittest.main()


