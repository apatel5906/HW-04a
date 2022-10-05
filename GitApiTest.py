#Arpit Patel
#The following code is to test the GitApi file.
import unittest

from GitApi import get_git_info


class TestTriangles(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(ValueError):
            get_git_info('NOT_EXIST_PEOPLE')

    def test_normal_case(self):
        self.assertEqual(get_git_info('richkempinski'), ('Repo: hellogitworld Number of commits: 30'
                                                         'Repo: helloworld Number of commits: 6'
                                                         'Repo: Mocks Number of commits: 10'
                                                         'Repo: Project1 Number of commits: 2'
                                                         'Repo: threads-of-life Number of commits: 1'))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()