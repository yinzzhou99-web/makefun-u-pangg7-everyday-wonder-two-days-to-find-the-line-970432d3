#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, about a small everyday moment of
wonder: the lift mirror, mid-yawn. Writes it to /output/entry.txt using
only the standard library, and never removes the output directory.
"""

from pathlib import Path
import os

LINE = "The elevator mirror caught me mid-yawn, and for a second I was a stranger politely ignoring me."


def check(line: str) -> None:
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if line != line.strip() or not line.strip():
        raise ValueError("line must not be blank or padded with spaces")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main() -> None:
    check(LINE)
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)  # the scorer reads as another user, never leave 0600/0660
    print(f"wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
