Implemented per `task.md` with minimal changes:

- Added CLI parser implementation in `duration_cli.py`.
- Added end-to-end CLI tests in `tests/test_e2e_cli.py`.

**What’s implemented**

- Python 3 CLI that accepts duration input tokens from command-line args and joins them into one input string: `duration_cli.py:68`, `duration_cli.py:80`.
- Full-string strict parsing for `\d+[hms]` tokens with optional whitespace only: `duration_cli.py:19`-`duration_cli.py:65`.
- Correct unit conversion and summation (including duplicate units): `duration_cli.py:11`-`duration_cli.py:12`, `duration_cli.py:60`-`duration_cli.py:63`.
- Clear invalid-input errors (empty input, missing number/unit, invalid unit, unexpected text) and non-zero exit on failure: `duration_cli.py:20`-`duration_cli.py:21`, `duration_cli.py:41`-`duration_cli.py:58`, `duration_cli.py:85`-`duration_cli.py:89`.
- Final result printed to stdout on success: `duration_cli.py:91`.

**End-to-end test**

- Added subprocess-based workflow tests that run the CLI as a real command:
  - valid case: `1h 5m 2s -> 3902`
  - invalid case: `1h-2m` returns non-zero with error text  
  File: `tests/test_e2e_cli.py:19`-`tests/test_e2e_cli.py:33`.

**Validation run**

- `python3 -m unittest -q tests/test_e2e_cli.py` passed (`Ran 2 tests ... OK`).
- Manual CLI checks:
  - `python3 duration_cli.py 1h30m` -> `5400`
  - `python3 duration_cli.py "1h 5m 2s"` -> `3902`
  - `python3 duration_cli.py 1x` -> `Error: Malformed token '1x': invalid unit 'x'.`
  - `python3 duration_cli.py` -> `Error: Input is empty. Provide at least one duration token.`