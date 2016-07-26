import unittest
from User import User

class UserIntegration(unittest.TestCase):

    def setUp(self):
        self.User = User('James', 'password')

    def tearDown(self):
        self.User = None

if __name__ == '__main__':
    unittest.main()
