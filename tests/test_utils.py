import unittest
#import os, sys
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from euler import utils


class PrimeTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_five_prime(self):
        self.assertTrue(utils.is_prime(5))

    def test_fibonacci_zero(self):
        self.assertEqual(utils.fibonacci(0), 1)
    
    def test_fibonacci_one(self):
        self.assertEqual(utils.fibonacci(1), 1)
    
    def test_fibonacci_two(self):
        self.assertEqual(utils.fibonacci(2), 2)


if __name__ == '__main__':
    unittest.main()