#!/usr/bin/env python3
"""CLI for parsing serialized durations and printing total seconds."""

from __future__ import annotations

import argparse
import re
import sys

TOKEN_RE = re.compile(r"\s*(\d+)([hms])")
INVALID_CHAR_RE = re.compile(r"[^0-9hms\s]")
UNIT_TO_SECONDS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(duration: str) -> int:
    """Parse a serialized duration string into total seconds."""
    if duration.strip() == "":
        raise ValueError("Input cannot be empty.")

    bad_char = INVALID_CHAR_RE.search(duration)
    if bad_char:
        ch = bad_char.group(0)
        idx = bad_char.start()
        raise ValueError(f"Invalid character '{ch}' at position {idx}.")

    pos = 0
    total = 0
    consumed_token = False

    while pos < len(duration):
        if duration[pos].isspace():
            pos += 1
            continue

        match = TOKEN_RE.match(duration, pos)
        if not match:
            excerpt = duration[pos : pos + 10]
            raise ValueError(f"Malformed token at position {pos}: '{excerpt}'.")

        value = int(match.group(1))
        unit = match.group(2)
        total += value * UNIT_TO_SECONDS[unit]
        pos = match.end()
        consumed_token = True

    if not consumed_token:
        raise ValueError("Input cannot be empty.")

    return total


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a serialized duration string into total seconds."
    )
    parser.add_argument(
        "duration",
        nargs="*",
        help="Duration tokens, e.g. 1h30m or 1h 5m 2s",
    )
    args = parser.parse_args(argv)

    duration_str = " ".join(args.duration)

    try:
        result = parse_duration(duration_str)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
