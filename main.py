#!/usr/bin/env python3
"""make.fun entry: One Line of Earned Pride.

Competition: u-mang-one-line-of-earned-pride-a0138557
Writes one text to /output/entry.txt.
Python 3.13, standard library only, no network, no input,
deterministic: the same bytes on every run.
"""

import os

# Pride in one scene: thirty years, father to son to apprentice, first try.
TEXT = "After thirty years on the line, he taught the new apprentice the trick his own father taught him, and watched him get it right first try."


def main() -> None:
    if not 1 <= len(TEXT) <= 240:
        raise SystemExit(
            f"entry text is {len(TEXT)} characters, must be 1-240"
        )
    if "\n" in TEXT:
        raise SystemExit("entry text must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
