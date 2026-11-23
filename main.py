#!/usr/bin/env python3
"""Write a complete story in exactly six words to /output/entry.txt.

The story: "He survived the war. Not peace."

Six words, one life: a man comes home from war, and the
peace he survived for is what finally takes him. Standard library
only, no network, no input files.
"""

import os

STORY = "He survived the war. Not peace."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit(f"expected 6 words, got {len(words)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    print(STORY)


if __name__ == "__main__":
    main()
