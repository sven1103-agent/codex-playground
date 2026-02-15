#!/usr/bin/env python3
"""CLI to parse serialized durations and print total seconds."""

from __future__ import annotations

import argparse
import re
import sys

TOKEN_RE = re.compile(r"(\d+)([hms])")
UNIT_SECONDS = {"h": 3600, "m": 60, "s": 1}


def parse_duration_to_seconds(duration: str) -> int:
    """Parse a serialized duration string and return total seconds."""
    if duration is None or duration.strip() == "":
        raise ValueError("Input is empty.")

    total = 0
    pos = 0
    matched_any = False
    length = len(duration)

    while pos < length:
        while pos < length and duration[pos].isspace():
            pos += 1
        if pos >= length:
            break

        match = TOKEN_RE.match(duration, pos)
        if not match:
            raise ValueError(
                f"Malformed token at position {pos + 1}. Expected <number><h|m|s>."
            )

        matched_any = True
        value = int(match.group(1))
        unit = match.group(2)
        total += value * UNIT_SECONDS[unit]
        pos = match.end()

    if not matched_any:
        raise ValueError("Input is empty.")

    return total


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a serialized duration and print total seconds."
    )
    parser.add_argument("duration", help="Duration string, e.g. '1h 5m 2s'")
    args = parser.parse_args(argv)

    try:
        print(parse_duration_to_seconds(args.duration))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
