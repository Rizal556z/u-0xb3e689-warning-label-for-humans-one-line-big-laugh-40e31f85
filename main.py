#!/usr/bin/env python3
"""Write the warning label for humans to /output/entry.txt.

Pure Python 3.13 standard library, no network, no model calls.
"""

import os

ENTRY = (
    "WARNING: This human will confidently explain things it does not "
    "understand, then double down when proven wrong. "
    "Do not operate while sleep-deprived."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read what we wrote and verify the gate constraints.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 160, f"length {len(written)} outside 1-160"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"
    assert not written.endswith("\n"), "entry must have no trailing newline"


if __name__ == "__main__":
    main()
