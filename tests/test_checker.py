
import unittest
from unittest.mock import patch, Mock

from src.checker import check_host


class TestNetworkHealthChecker(unittest.TestCase):

    def test_empty_host(self):
        with self.assertRaises(ValueError):
            check_host("")

    @patch("src.checker.subprocess.run")
    @patch("src.checker.platform.system", return_value="Windows")
    def test_host_up(self, mock_system, mock_run):
        mock_run.return_value = Mock(
            returncode=0,
            stdout="Reply from 127.0.0.1: time=2ms",
            stderr=""
        )

        result = check_host("127.0.0.1")

        self.assertEqual(result["status"], "UP")
        self.assertEqual(result["latency_ms"], 2.0)

    @patch("src.checker.subprocess.run")
    @patch("src.checker.platform.system", return_value="Windows")
    def test_host_down(self, mock_system, mock_run):
        mock_run.return_value = Mock(
            returncode=1,
            stdout="Request timed out.",
            stderr=""
        )

        result = check_host("192.0.2.1")

        self.assertEqual(result["status"], "DOWN")
        self.assertIsNone(result["latency_ms"])


if __name__ == "__main__":
    unittest.main()
