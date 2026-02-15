#!/usr/bin/env python3
"""CLI for parsing serialized duration strings into total seconds."""

from __future__ import annotations

import argparse
import re
import sys

TOKEN_RE = re.compile(r"(\d+)([hms])")
UNIT_SECONDS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(text: str) -> int:
    if text is None or text.strip() == "":
        raise ValueError("Input cannot be empty.")

    total_seconds = 0
    position = 0
    token_count = 0

    for match in TOKEN_RE.finditer(text):
        gap = text[position:match.start()]
        if gap.strip():
            raise ValueError(f"Unexpected text between tokens: '{gap}'.")

        value = int(match.group(1))
        unit = match.group(2)
        total_seconds += value * UNIT_SECONDS[unit]

        position = match.end()
        token_count += 1

    if token_count == 0:
        raise ValueError("Malformed duration: expected tokens like '1h', '30m', or '45s'.")

    trailing = text[position:]
    if trailing.strip():
        raise ValueError(f"Unexpected trailing text: '{trailing}'.")

    return total_seconds


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse a serialized duration string and print total seconds."
    )
    parser.add_argument(
        "duration",
        nargs="+",
        help="Duration string made of <integer><unit> tokens (units: h, m, s).",
    )

    args = parser.parse_args(argv)
    duration_text = " ".join(args.duration)

    try:
        total_seconds = parse_duration(duration_text)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(total_seconds)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
