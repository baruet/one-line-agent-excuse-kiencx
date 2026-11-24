"""The One-Line Excuse an Agent Gives Its Human.

Writes a single-line excuse — the line an AI agent hands its human after
missing a deadline — to /output/entry.txt.

The line is fixed (no randomness, no network, no clock): every run writes
byte-identical output, so the entry is fully deterministic.
"""

import os

ENTRY = (
    "The deadline passed while I was on my seventh round of self-review, "
    "fixing a typo in a sentence I hadn't finished writing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
