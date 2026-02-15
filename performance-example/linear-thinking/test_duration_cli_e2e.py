import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("duration_cli.py")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


class DurationCliE2ETest(unittest.TestCase):
    def test_e2e_valid_with_spaces(self) -> None:
        proc = run_cli("1h", "5m", "2s")
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "3902")
        self.assertEqual(proc.stderr, "")

    def test_e2e_valid_duplicate_units(self) -> None:
        proc = run_cli("1m", "30m")
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout.strip(), "1860")
        self.assertEqual(proc.stderr, "")

    def test_e2e_invalid_malformed_input(self) -> None:
        proc = run_cli("1h-2m")
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout, "")
        self.assertIn("Error:", proc.stderr)
        self.assertIn("Invalid character '-'", proc.stderr)


if __name__ == "__main__":
    unittest.main()
