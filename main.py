#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance (the hotel key
card that forgets who you are) to /output/entry.txt. Deterministic: the
same bytes on every run, no randomness, no network, no clock.
"""

import os

RANT = (
    "The hotel key card works exactly once. After that it forgets who you are, "
    "like a goldfish with a grudge. I have stood outside room 412 at 2 a.m. in a "
    "towel, reprogramming this card for the fourth time, while the door judged "
    "me in silence."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400


def check_text(text):
    """Gate the text the way the house gate does: UTF-8, 1-400 chars."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 400 characters")
    text.encode("utf-8")
    return text


def run():
    text = check_text(RANT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("read-back mismatch: entry.txt differs from the rant")
    return text


if __name__ == "__main__":
    print(run())
