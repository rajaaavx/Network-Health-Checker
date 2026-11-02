import unittest
from unittest.mock import patch, Mock

from src.checker import check_host

class TestNetworkHealthChecker(unittest.TestCase):
    def test_empty_host(self):
        with self.assertRaises(ValueError):
            check_host("")

if __name__ == "__main__":
    unittest.main()