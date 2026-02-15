Implemented per `task.md` with a Python 3 CLI + end-to-end test.

**What I changed**
- Added parser + CLI in `duration_cli.py:14` and `duration_cli.py:48`.
- Full-string validation is enforced by ordered token matching; malformed/extra text is rejected with clear errors in `duration_cli.py:30`.
- Added end-to-end CLI tests in `test_duration_cli_e2e.py:15` (valid + invalid workflow via subprocess).

**Behavior**
- Valid input example:
  - `python3 duration_cli.py "1h30m"` prints `5400` to stdout.
- Invalid input example:
  - `python3 duration_cli.py "1h-2m"` prints `Error: Malformed token at position 3. Expected <number><h|m|s>.` to stderr and exits non-zero.

**Validation run**
- `python3 -m unittest -q`  
  - Ran 2 tests, all passed.