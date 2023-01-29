import unittest
from is_valid_walk import is_valid_walk


class TestMultiply(unittest.TestCase):
    def test_check_direction(self):
        self.assertTrue(
            is_valid_walk(['n','s','n','s','n','s','n','s','n','s']),
            "Should return True")
        self.assertFalse(
            is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']),
            "Should return False")
        self.assertFalse(
            is_valid_walk(['w']),
            "Should return False")
        self.assertFalse(
            is_valid_walk(['n','n','n','s','n','s','n','s','n','s']),
            "Should return False")


if __name__ == "__main__":
    unittest.main()
