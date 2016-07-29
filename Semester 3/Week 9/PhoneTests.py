import unittest

class Phone():

    def __init__(self):
        # Initialise the class
        self.isOn = False

    def switchOn(self):
        self.isOn = True

class PhoneTests(unittest.TestCase):

    def setUp(self):
        self.Phone = Phone()

    def tearDown(self):
        self.Phone = None

    def test_phoneSwitchesOn(self):
        self.assertFalse(self.Phone.isOn)
        self.Phone.switchOn()
        self.assertTrue(self.Phone.isOn)


if __name__ == '__main__':
    unittest.main()
