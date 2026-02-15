# Task: Parse a Serialized Duration Format

## Objective

Implement a Python 3 CLI application that parses a serialized duration
string and converts it into the total number of seconds.

------------------------------------------------------------------------

## Input Format

The input is a string representing a duration composed of one or more
time tokens.

Each token consists of:

-   A non-negative integer
-   Immediately followed by a unit:
    -   `h` for hours
    -   `m` for minutes
    -   `s` for seconds

Tokens may optionally be separated by whitespace.

### Valid Examples

-   `1h30m`
-   `45m`
-   `2h`
-   `90s`
-   `1h 5m 2s`
-   `1m 30m` (duplicate units are allowed and should be summed)

------------------------------------------------------------------------

## Output

The program must print the total duration in seconds to stdout.

### Example Conversions

  Input        Output
  ------------ --------
  `1h30m`      5400
  `45m`        2700
  `2h`         7200
  `90s`        90
  `1h 5m 2s`   3902

------------------------------------------------------------------------

## Validation Rules

The implementation must:

-   Reject empty input.
-   Reject inputs containing invalid characters.
-   Reject malformed tokens (e.g., `1x`, `h`, `1`, `1h-2m`).
-   Reject unexpected text between valid tokens.
-   Provide meaningful error messages for invalid inputs.

------------------------------------------------------------------------

## Technical Requirements

-   The solution MUST be implemented in Python 3.
-   The solution MUST provide a CLI interface to accept the duration
    string as input.
-   The solution MUST print the result to stdout.
-   The solution MUST include at least one end-to-end test verifying the
    full workflow.
-   The entire input string must be validated --- no partial parsing
    allowed.

------------------------------------------------------------------------

## Definition of Done

-   The CLI runs successfully from the command line.
-   Valid inputs return correct results.
-   Invalid inputs produce clear error messages.
-   The end-to-end test executes successfully.
