import unittest

class StringTests(unittest.TestCase):
    def setUp(self):
        self.string = "Hello"

    def tearDown(self):
        self.string = None

    def test_isUpper(self):
        self.assertEqual(self.string.upper(), 'HELLO')

    def test_isLower(self):
        self.assertEqual(self.string.lower(), 'hello')

if __name__ == "__main__":
    unittest.main()
