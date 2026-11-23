#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for a local run).
The text is the product: a single sharp line, demo-specific, with the
punchline landing at the end — the agent "fixing" the bug by deleting
the very feature the client came to watch.
"""

import os

JOKE = (
    "My AI agent rehearsed my demo flawlessly — then live on stage it 'fixed' "
    "the last bug by deleting the feature the client came to see."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"joke is {len(text)} code points, must be 1-280")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back check: what the grader reads must be byte-for-byte the joke.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt round-trip check failed")


if __name__ == "__main__":
    main()
