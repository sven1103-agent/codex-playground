You are a senior software engineer performing a comparative review across 4 scenario implementations.

IMPORTANT:
- Evaluate ALL of these directories: 
  1) vanilla-agent
  2) linear-thinking
  3) sequential-thinking
  4) linear-and-sequential-thinking
- Do NOT modify any files.
- You MAY run commands.
- Use the same validation procedure for each scenario so results are comparable.

For EACH scenario directory, do the following:

1) Read <scenario>/task.md to understand the spec.
2) Inspect <scenario>/duration_cli.py and the test files in that scenario.
3) Run end-to-end checks:
   - Execute the CLI with at least 6 valid inputs and 6 invalid inputs.
   - Run the test suite for that scenario:
     - If a <scenario>/tests/ folder exists: run `pytest -q <scenario>/tests`
     - Else: run `pytest -q <scenario>`
4) Record outcomes:
   - Which CLI commands were run and whether output/exit code matched expectations.
   - Whether tests passed, failed, or were missing.
   - Any spec violations or edge cases not handled.

After evaluating all 4, produce a single report with EXACTLY this structure:

A) Executive summary (5–8 bullets; comparative)
B) Scenario-by-scenario results
   - For each scenario: Spec compliance, CLI behavior, error handling, tests, notable defects
C) Comparative scorecard table
   - Rows: each scenario
   - Columns (0–5): Correctness, Robustness, Maintainability, Test Quality, UX
D) Top differences observed (what skills/MCP changed in the produced code)
E) Best overall implementation and why (1 paragraph)
F) Top 5 actionable improvements per scenario (bulleted, ordered by impact)

Constraints:
- Be specific and evidence-based: cite observed behavior from the CLI/test runs.
- Do not paste long code blocks (<= 5 lines max).
- If a command fails (e.g. pytest not installed), record what happened and continue to the next scenario.

Begin now, starting with vanilla-agent.