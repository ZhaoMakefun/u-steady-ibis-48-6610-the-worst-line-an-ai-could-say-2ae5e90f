#!/usr/bin/env python3
# The worst line an AI could say: it quotes its training data, gives
# you a probability, and asks you to confirm dinner. Romance, as
# computed by a machine that has never been on a date.

import sys
from os import getenv
from pathlib import Path

LINE = "I have analysed 10,000 conversations and calculate a 94% chance you will enjoy dinner with me, so please confirm your availability."
CAP = 140


def produce():
    candidate = LINE.strip()
    problems = []
    if not candidate:
        problems.append("line is empty")
    if len(candidate) > CAP:
        problems.append(f"line is {len(candidate)} chars, over the {CAP} cap")
    if set(candidate) & set("\r\n"):
        problems.append("line must not contain a line break")
    # Report every problem at once instead of failing on the first one.
    if problems:
        print("entry rejected: " + "; ".join(problems), file=sys.stderr)
        raise SystemExit(1)
    candidate.encode("utf-8")
    out = Path(getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    out.mkdir(parents=True, exist_ok=True)
    out.joinpath("entry.txt").write_text(candidate, encoding="utf-8")


produce()
