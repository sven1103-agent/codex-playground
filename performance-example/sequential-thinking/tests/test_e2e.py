import subprocess
import sys
from pathlib import Path
import unittest


class DurationCliE2ETest(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        root = Path(__file__).resolve().parents[1]
        cli_path = root / "duration_cli.py"
        return subprocess.run(
            [sys.executable, str(cli_path), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_valid_duration(self) -> None:
        result = self.run_cli("1h", "5m", "2s")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "3902")
        self.assertEqual(result.stderr.strip(), "")

    def test_invalid_duration(self) -> None:
        result = self.run_cli("1h-2m")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Error:", result.stderr)
        self.assertIn("Unexpected", result.stderr)


if __name__ == "__main__":
    unittest.main()
