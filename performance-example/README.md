# Codex Scenario Benchmark

This repository contains a controlled benchmark for evaluating how
different **agent configurations** influence implementation quality for
the same programming task.

The goal is to compare:

-   🟢 Vanilla agent (no structured reasoning guidance)
-   🔵 Linear thinking skill
-   🟡 Sequential Thinking MCP tool
-   🟣 Combination of Linear Thinking + Sequential Thinking

The benchmark focuses on implementation quality, robustness, CLI
ergonomics, and test quality.

------------------------------------------------------------------------

# 🎯 Purpose

This benchmark investigates:

-   Does structured reasoning improve implementation quality?
-   Does MCP-based planning lead to more robust code?
-   Does combining reasoning methods improve or degrade results?
-   What trade-offs appear in CLI design, validation, and test rigor?

The task remains identical across all scenarios to ensure comparability.

------------------------------------------------------------------------

# 📦 Repository Structure

    performance-example/
    ├── vanilla-agent/
    ├── linear-thinking/
    ├── sequential-thinking/
    ├── linear-and-sequential-thinking/
    ├── runs/
    └── run-tasks.py

Each scenario contains:

    <scenario>/
    ├── AGENTS.md
    ├── task.md
    ├── duration_cli.py
    └── tests/ or test_*.py

------------------------------------------------------------------------

# 🧠 Scenarios

## 1️⃣ vanilla-agent

Baseline implementation without structured reasoning.

## 2️⃣ linear-thinking

Enforces strict step-by-step reasoning.

## 3️⃣ sequential-thinking

Requires MCP-based structured planning.

## 4️⃣ linear-and-sequential-thinking

Combines MCP planning and linear execution.

------------------------------------------------------------------------

# 📄 Task Overview

The task is defined in `task.md` for each scenario:

-   Parse serialized duration (e.g., `1h30m`)
-   Convert to total seconds
-   Provide CLI interface
-   Print result to stdout
-   Handle invalid input robustly
-   Include end-to-end test

------------------------------------------------------------------------

# ▶️ Running the Benchmark

From repository root:

    python run-tasks.py

Results are written to:

    runs/<timestamp>/

Each run produces:

-   `<scenario>.events.jsonl`
-   `<scenario>.final.md`
-   `<scenario>.stderr.txt`
-   `summary.json`

------------------------------------------------------------------------

# 📊 Evaluation Criteria

Validation matrix includes:

### Valid Inputs

-   1h30m
-   45m
-   2h
-   90s
-   1h 5m 2s
-   1m 30m

### Invalid Inputs

-   empty
-   1x
-   h
-   1
-   1h-2m
-   1h foo

Scoring (0--5):

-   Correctness
-   Robustness
-   Maintainability
-   Test Quality
-   UX

------------------------------------------------------------------------

# 🚧 Open Improvements

## Environment

-   [ ] Install and enforce pytest before evaluation
-   [ ] Add reproducible virtual environment setup

## Evaluation

-   [ ] Automate CLI matrix inside orchestrator
-   [ ] Generate CSV scorecard
-   [ ] Track token usage per scenario

## Benchmark Extensions

-   [ ] Add Java version
-   [ ] Add static analysis
-   [ ] Add complexity metrics
-   [ ] Add performance measurements

------------------------------------------------------------------------

# 🧩 Research Questions

-   Does enforced linear reasoning improve robustness?
-   Does MCP planning improve validation completeness?
-   Does combining reasoning modes create regressions?
-   What is the token overhead of structured reasoning?

------------------------------------------------------------------------

# 🏁 Summary

This repository is an experimental framework for studying how structured
reasoning and MCP-based planning affect coding agent output quality.

It evaluates behavioral differences, not model performance differences.
