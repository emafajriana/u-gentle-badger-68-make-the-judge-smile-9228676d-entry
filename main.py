#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes a single line about one small good thing from today to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that
environment variable is set). Standard library only.
"""

import os

# The entry itself: one line, well inside the 1-200 character gate.
LINE = (
    "At 6 a.m. the neighbour's rooster crowed right outside our window, "
    "my grandma murmured 'amen' in her sleep, "
    "and the whole house woke up laughing."
)


def entry_path() -> str:
    """Where the grader expects the entry file to land."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def write_entry() -> str:
    """Write LINE to the entry path and return the path used."""
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def verify(path: str) -> bool:
    """Read the file back and check it against the gate: the exact
    line, 1-200 characters of UTF-8 text, not only whitespace."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    return text == LINE and 1 <= len(text) <= 200 and bool(text.strip())


def main() -> int:
    path = write_entry()
    if not verify(path):
        print(f"entry at {path} failed read-back verification")
        return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
