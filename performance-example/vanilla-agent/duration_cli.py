#!/usr/bin/env python3
"""CLI for parsing serialized duration strings into total seconds."""

from __future__ import annotations

import argparse
import re
import sys


_TOKEN_RE = re.compile(r"(\d+)([hms])")
_MULTIPLIERS = {"h": 3600, "m": 60, "s": 1}


class DurationParseError(ValueError):
    """Raised when a duration string is invalid."""


def parse_duration_to_seconds(text: str) -> int:
    if text is None or text.strip() == "":
        raise DurationParseError("Input is empty. Provide at least one duration token.")

    total_seconds = 0
    position = 0
    length = len(text)

    while position < length:
        while position < length and text[position].isspace():
            position += 1

        if position >= length:
            break

        match = _TOKEN_RE.match(text, position)
        if not match:
            token_start = position
            while position < length and not text[position].isspace():
                position += 1
            bad_chunk = text[token_start:position]

            if bad_chunk and bad_chunk[0] in "hms":
                raise DurationParseError(
                    f"Malformed token '{bad_chunk}': missing number before unit."
                )

            if bad_chunk.isdigit():
                raise DurationParseError(
                    f"Malformed token '{bad_chunk}': missing unit (expected h, m, or s)."
                )

            if bad_chunk and bad_chunk[-1].isalpha() and bad_chunk[-1] not in _MULTIPLIERS:
                raise DurationParseError(
                    f"Malformed token '{bad_chunk}': invalid unit '{bad_chunk[-1]}'."
                )

            raise DurationParseError(
                f"Unexpected text '{bad_chunk}' in duration input."
            )

        value = int(match.group(1))
        unit = match.group(2)
        total_seconds += value * _MULTIPLIERS[unit]
        position = match.end()

    return total_seconds


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse a serialized duration string and print total seconds."
    )
    parser.add_argument(
        "duration",
        nargs="*",
        help="Duration string, e.g. '1h30m' or '1h 5m 2s'.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    raw_input = " ".join(args.duration)

    try:
        total = parse_duration_to_seconds(raw_input)
    except DurationParseError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
