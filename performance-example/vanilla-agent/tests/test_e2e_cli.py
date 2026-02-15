import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "duration_cli.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        capture_output=True,
        text=True,
    )


class TestDurationCliE2E(unittest.TestCase):
    def test_cli_valid_input_end_to_end(self) -> None:
        result = run_cli("1h", "5m", "2s")

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "3902")
        self.assertEqual(result.stderr, "")

    def test_cli_invalid_input_end_to_end(self) -> None:
        result = run_cli("1h-2m")

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("Error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
