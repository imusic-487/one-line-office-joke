#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life to /output/entry.txt.
Python 3.13 standard library only, no network. Deterministic: every run
writes the exact same bytes.
"""

import os

JOKE = (
    "My calendar is so full that my lunch break now has a waitlist, "
    "and the waitlist has a meeting to discuss the waitlist."
)


def main() -> None:
    # Gate self-check (competition gate: 1-200 characters, a single line,
    # not only whitespace).
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate needs 1-200"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
