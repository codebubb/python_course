import unittest
import functions

class FunctionsTest(unittest.TestCase):

    # def test_additionWorks(self):
    #     self.assertEqual(functions.add(2,2), 4)
    #     self.assertEqual(functions.add(2,5), 7)
    #     self.assertEqual(functions.add(1,99), 100)
    #     self.assertNotEqual(functions.add(12,76), 78)

    def test_countFunction(self):
        self.assertEqual(functions.count('The,quick brown fox'), 4)

if __name__ == '__main__':
    unittest.main()
