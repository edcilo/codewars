import unittest
from is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0), "Should be False")
        self.assertFalse(is_prime(1), "Should be False")
        self.assertTrue(is_prime(2), "Should be True")
        self.assertTrue(is_prime(73), "Should be True")
        self.assertFalse(is_prime(75), "Should be False")
        self.assertTrue(is_prime(839), "Should be True")
        self.assertFalse(is_prime(10000000000000), "Should be False")
        self.assertFalse(is_prime(-1), "Should be False")


if __name__ == "__main__":
    unittest.main()
