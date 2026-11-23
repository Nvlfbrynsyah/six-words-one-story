"""make.fun entry for "Six Words, One Story".

Writes a single six-word story to a file, deterministically and with no
trailing newline. The output path comes from SIXWORDS_OUTPUT when set,
otherwise /output/entry.txt.
"""

import os
import sys

STORY = "She planted his ashes. Roses bloomed."

OUTPUT_PATH = os.environ.get("SIXWORDS_OUTPUT", "/output/entry.txt")


def main():
    words = STORY.split()
    if len(words) != 6:
        sys.exit(f"error: STORY must be exactly 6 words, found {len(words)}")

    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(OUTPUT_PATH, "wb") as f:
        f.write(STORY.encode("utf-8"))


if __name__ == "__main__":
    main()
