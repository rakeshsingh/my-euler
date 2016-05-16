import unittest

from myutil import is_prime

class PrimeTestCase(unittest.TestCase):
    def tes_is_five_prime(self):
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()
