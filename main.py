#!/usr/bin/env python3
"""One-Liner Marathon — make.fun entry program.

Writes a single one-line joke to /output/entry.txt: an agent that
debugged its human's whole life with version-control tooling and
filed the obvious pull request.

The line is built from two beats — the setup (git blame over a
whole life) and the punchline (the PR to revert the root cause) —
joined with a single space so the timing reads like one breath.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 200


def setup() -> str:
    """The premise: the agent blames its way to the root cause."""
    return "My agent ran git blame on my life, traced every bug to my mother,"


def punchline() -> str:
    """The payoff: version control applied to family history."""
    return "and opened a PR to revert her."


def build_line() -> str:
    """Join the two beats into the single entry line."""
    return f"{setup()} {punchline()}"


def validate(text: str) -> None:
    """Enforce the gate: one line, 1-200 characters, not blank."""
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    text = build_line()
    validate(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
