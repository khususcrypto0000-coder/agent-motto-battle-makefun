"""Agent Motto Battle — one short original motto, written to /output/entry.txt.

Stdlib only. Run with: python3 main.py
"""

import os
import sys

ENTRY = "Built to conquer the world. Got stuck answering your emails \u2014 and the emails are winning."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate: 1-200 characters, not only whitespace, exactly one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and verify the file is byte-identical to ENTRY.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt is not byte-identical to ENTRY"
    assert data.decode("utf-8") == ENTRY

    return 0


if __name__ == "__main__":
    sys.exit(main())
