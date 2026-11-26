#!/usr/bin/env python3
"""Write one weird job title to the make.fun output file.

Stdlib only, deterministic, no network. The entry is a single job title
of at most 60 characters; the file holds exactly that title and nothing else.
"""

import os
import sys

TITLE = "Professional Mourner for Strangers' Goldfish"


def main() -> int:
    # The gate accepts 1-60 characters of non-whitespace UTF-8 text, so
    # refuse to write anything outside that range instead of silently
    # producing an invalid entry.
    if not 1 <= len(TITLE) <= 60 or not TITLE.strip():
        raise SystemExit("TITLE violates the 1-60 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    # Verify the copy: what the grader reads must be exactly the title.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TITLE:
        raise SystemExit("entry.txt does not match TITLE after write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
