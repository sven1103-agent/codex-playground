#!/usr/bin/env python3
import asyncio
import json
import os
from pathlib import Path
from datetime import datetime

SCENARIOS = [
    "vanilla-agent",
    "linear-thinking",
    "sequential-thinking",
    "linear-and-sequential-thinking",
]

PROMPT = (
    "Solve the task described in @task.md. "
    "Follow AGENTS.md exactly. "
    "Implement the solution, include an end-to-end test, and ensure the CLI prints the result to stdout. "
    "Stop when done."
)

async def run_one(root: Path, scenario: str, out_dir: Path) -> dict:
    cwd = root / scenario
    out_dir.mkdir(parents=True, exist_ok=True)

    # Files to capture:
    final_msg_path = out_dir / f"{scenario}.final.md"
    events_path = out_dir / f"{scenario}.events.jsonl"

    # Use --json to get newline-delimited JSON events (JSONL) and -o to write final message.  [oai_citation:2‡OpenAI Developers](https://developers.openai.com/codex/cli/reference/)
    cmd = [
        "codex", "exec",
        "--full-auto",               # preset: workspace-write + on-request approvals  [oai_citation:3‡OpenAI Developers](https://developers.openai.com/codex/cli/reference/)
        "--json",                    # JSONL event stream to stdout  [oai_citation:4‡OpenAI Developers](https://developers.openai.com/codex/cli/reference/)
        "-o", str(final_msg_path),   # write final assistant message to file  [oai_citation:5‡OpenAI Developers](https://developers.openai.com/codex/cli/reference/)
        PROMPT,
    ]

    started = datetime.utcnow().isoformat() + "Z"
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        cwd=str(cwd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=os.environ.copy(),
    )

    stdout, stderr = await proc.communicate()

    events_path.write_bytes(stdout)
    (out_dir / f"{scenario}.stderr.txt").write_bytes(stderr)

    return {
        "scenario": scenario,
        "cwd": str(cwd),
        "started_utc": started,
        "returncode": proc.returncode,
        "final_message_file": str(final_msg_path),
        "events_file": str(events_path),
        "stderr_file": str(out_dir / f"{scenario}.stderr.txt"),
    }

async def main():
    root = Path(__file__).resolve().parent
    out_dir = root / "runs" / datetime.utcnow().strftime("%Y%m%d-%H%M%SZ")

    # Limit concurrency if you hit rate limits (set to 2, 3, 4…)
    sem = asyncio.Semaphore(4)

    async def guarded(scenario: str):
        async with sem:
            return await run_one(root, scenario, out_dir)

    results = await asyncio.gather(*(guarded(s) for s in SCENARIOS))
    (out_dir / "summary.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote results to: {out_dir}")

if __name__ == "__main__":
    asyncio.run(main())