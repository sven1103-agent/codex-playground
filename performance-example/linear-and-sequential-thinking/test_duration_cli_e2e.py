import subprocess
import sys
import unittest


def run_cli(arg: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "duration_cli.py", arg],
        capture_output=True,
        text=True,
        check=False,
    )


class DurationCliE2ETest(unittest.TestCase):
    def test_cli_valid_input_end_to_end(self) -> None:
        result = run_cli("1h 5m 2s")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "3902")
        self.assertEqual(result.stderr, "")

    def test_cli_invalid_input_end_to_end(self) -> None:
        result = run_cli("1h-2m")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Error:", result.stderr)
        self.assertIn("Malformed token", result.stderr)


if __name__ == "__main__":
    unittest.main()
