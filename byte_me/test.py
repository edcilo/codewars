import unittest
from total_bytes import total_bytes


class TestTotalBytes(unittest.TestCase):
    def test_total_bytes(self):
        self.assertEqual(total_bytes(123), 28, "Should be 28")
        self.assertEqual(total_bytes([1, 2]), 72, "Should be 72")
        self.assertEqual(total_bytes((1, 2)), 56, "Should be 56")
        self.assertEqual(total_bytes("hello"), 54, "Should be 54")
        self.assertEqual(total_bytes(999_999), 28, "Should be 28")
        self.assertEqual(total_bytes("¡◢龘"), 80, "Should be 80")


if __name__ == "__main__":
    unittest.main()
