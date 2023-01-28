import unittest
from multiply import multiply


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 1), 2, "Should be 2")


if __name__ == "__main__":
    unittest.main()
