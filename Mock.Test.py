"""



"""
from GitApi import get_repos, retrieve_commits
from unittest import mock
import unittest


class MockGitApi(unittest.TestCase):

    @mock.patch('GitApi.get_repos')
    def mock_get_repos_2(self, mock_repo_names):
        mock_repo_names.return_value = ['csp',' hellogitworld','helloworld','Mocks','Project1','richkempinski.github.io','threads-of-life' ,'try_nbdev','try_nbdev2']

        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 9, "User 'richkempinski' has 9 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)
        self.assertIn('csp',repos)
        self.assertIn('richkempinskie.github.io',repos)
        self.assertIn('Mocks',repos)
        self.assertIn('try_nbdev',repos)
        self.assertIn('try_nbdev2',repos)


    @mock.patch('GitApi.get_repos')
    def mock_invalid_user(self, mock_repo_name):
        mock_repo_name.return_value = []
        repos = get_repos('sdvnjnWfassvav')
        self.assertEqual(len(repos), 0, "Error: Invalid Username")


if __name__ == '__main__':
    print("Unit Test: Start")
    unittest.main()

