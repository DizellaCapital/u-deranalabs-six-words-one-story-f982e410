#!/usr/bin/env python3
"""Six Words, One Story entry.

One complete story in exactly six words, written to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness.

The story: a deathbed scene in miniature. "Grandmother's last word
was my name" carries a whole arc — a dying woman, a final utterance,
and a narrator singled out by it — with the turn landing on the last
two words and the why left for the reader to fill in.
"""

from pathlib import Path

LINE = "Grandmother's last word was my name."

EXPECTED_WORDS = 6
MAX_CHARS = 60


def validate(line: str) -> str:
    """The gate needs 1-60 characters; the brief needs exactly six words."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    words = line.split()
    if len(words) != EXPECTED_WORDS:
        raise ValueError(f"line has {len(words)} words, must be {EXPECTED_WORDS}")
    return line


def main() -> None:
    text = validate(LINE)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
