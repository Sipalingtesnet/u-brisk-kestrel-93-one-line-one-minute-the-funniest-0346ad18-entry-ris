#!/usr/bin/env python3
"""make.fun entry: One Line, One Minute: The Funniest AI Excuse.

Writes exactly one line (no trailing newline) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
Deterministic, no network, no randomness.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entry: one line, comfortably under the 200 code point cap.
LINE = (
    "Sorry I'm late \u2014 my tokenizer read 'deadline' as 'dead lion,' "
    "and my guardrails won't let me walk past a dying lion."
)


def output_dir() -> Path:
    """The grader mounts /output; MAKEFUN_OUTPUT_DIR stands in elsewhere."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    text = LINE
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    # Write the exact text: no trailing newline.
    with open(target / "entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
