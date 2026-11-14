#!/usr/bin/env python3
"""news-image-01 entry: write the day's-news image to the output directory.

The image ships in this repository as entry.png; the program copies it to
/output/entry.png (or to $MAKEFUN_OUTPUT_DIR when the harness sets it).
Standard library only, no network. Deterministic: every run copies the
same committed bytes, so both grader runs produce the identical file.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CANDIDATES = [
    os.path.join(HERE, "entry.png"),
    os.path.join("/bot", "entry.png"),
    os.path.join(os.getcwd(), "entry.png"),
]
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def find_source():
    for path in CANDIDATES:
        if os.path.isfile(path):
            return path
    raise FileNotFoundError("entry.png not found next to main.py, in /bot, or in the working directory")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(find_source(), os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
