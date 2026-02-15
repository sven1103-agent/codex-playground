Implemented per `task.md` with minimal changes:

- Added CLI parser in `duration_cli.py:14`:
  - Strict full-input parsing of `(\d+)([hms])` tokens.
  - Allows whitespace between tokens and sums duplicate units.
  - Rejects empty input, malformed input, invalid/interleaved text, and trailing unexpected text with clear errors.
  - Prints total seconds to stdout on success (`duration_cli.py:63`).
  - Prints error to stderr and exits non-zero on failure (`duration_cli.py:59`).

- Added end-to-end tests in `tests/test_e2e.py:7`:
  - Valid full CLI workflow (`1h 5m 2s` -> `3902`) (`tests/test_e2e.py:18`).
  - Invalid full CLI workflow (`1h-2m`) returns non-zero and clear error (`tests/test_e2e.py:24`).

Validation run:

- `python3 -m unittest discover -s tests -v` -> 2 tests passed.
- Manual checks:
  - `python3 duration_cli.py 1h30m` -> `5400`
  - `python3 duration_cli.py 1m 30m` -> `1860`
  - `python3 duration_cli.py 1h-2m` -> `Error: Unexpected text between tokens: '-'.`
  - `python3 duration_cli.py "   "` -> `Error: Input cannot be empty.`