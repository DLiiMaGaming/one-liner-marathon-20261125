#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one one-line comedy joke to /output/entry.txt.

The joke is fixed text: deterministic, no network, no secrets, no
environment input — the grader runs this file twice and both runs must
produce the same bytes.
"""

import os
import sys

JOKE = (
    "My agent ran git blame on my life, traced every bug to my mother, "
    "and opened a PR to revert her."
)


def build_entry_text():
    """Return the entry text exactly as it must land in /output/entry.txt."""
    return JOKE


def write_entry(path, text):
    """Write text to path, creating the parent directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    write_entry("/output/entry.txt", build_entry_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
