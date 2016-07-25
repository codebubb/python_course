''''''''''''''''''''''''''''''''
def add(*nums):
    return sum(nums)

def average(*nums):
    return sum(nums) / len(nums)
''''''''''''''''''''''''''''''''


import unittest

class TestMathsFunctions(unittest.TestCase):
    def test_add(self):
        self.assertTrue(isinstance(add(1,2,3), int))
        self.assertEqual(   add(1,2,3),     6)

    def test_average(self):
        self.assertTrue(isinstance(average(1,2,3), int))
        self.assertEqual(   average(1,2,3),  2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathsFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
