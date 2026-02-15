1. Inputs/outputs  
- Implemented a Python 3 CLI in `duration_cli.py` that accepts duration tokens as positional args, parses the full input, and prints total seconds to stdout.  
- On invalid input, it prints a meaningful `Error: ...` message to stderr and exits non-zero.

2. Edge cases handled  
- Empty input (`Input cannot be empty.`)  
- Invalid characters with position (`Invalid character 'x' at position N.`)  
- Malformed tokens / partial parsing failures (`Malformed token at position N: '...'`)  
- Unexpected text between tokens  
- Duplicate units are summed (`1m 30m` -> `1860`)

3. Algorithm  
- Join CLI args into one string.  
- Reject empty input.  
- Reject any non `[0-9hms\\s]` characters.  
- Parse strictly left-to-right using token regex `(\d+)([hms])` with whitespace handling, ensuring the entire string is consumed.  
- Convert units using `h=3600`, `m=60`, `s=1` and accumulate.

4. Implementation steps completed  
- Added CLI parser and core logic in `duration_cli.py`.  
- Added end-to-end workflow tests in `test_duration_cli_e2e.py` using `unittest` + subprocess (no external deps).  
- Kept changes minimal and focused on `task.md` requirements.

5. Tests and validation  
- Executed: `python3 -m unittest -q test_duration_cli_e2e.py`  
- Result: `Ran 3 tests ... OK`  
- Manual CLI checks:  
  - `python3 duration_cli.py 1h30m` -> `5400`  
  - `python3 duration_cli.py 1h 5m 2s` -> `3902`  
  - `python3 duration_cli.py 1m 30m` -> `1860`  
  - `python3 duration_cli.py 1h-2m` -> error to stderr, exit code `1`

Files changed: `duration_cli.py`, `test_duration_cli_e2e.py`.