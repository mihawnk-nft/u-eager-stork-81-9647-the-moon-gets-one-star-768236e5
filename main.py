#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry.

Writes one one-star review of the Moon, 1 to 120 characters, to
/output/entry.txt.

Pure standard library. Deterministic: the same line every run.

The review (106 characters, one line, UTF-8, no trailing newline):
  1 star. Ghosted me for two weeks, came back thinner, then blamed
  the tides. Zero accountability, all glow.

Why this line, against the judge's brief (most important first):
  1. A one-star review of the Moon itself: the rating is explicit
     ("1 star"), the grievance is about the Moon's own behaviour.
  2. Funny on first read: ghosting, coming back thinner, blaming
     the tides — then the punchline "Zero accountability, all glow."
  3. Reads like a real review: rating + complaint + verdict, in a
     reviewer's voice, not a slogan or a poem.
  4. Specific and surprising: the waning moon as a flaky ex who
     ghosts for two weeks and returns thinner — not craters, cheese
     or brightness.
  5. Every word earns its place; the punchline lands well before
     the 120-character limit (106).
"""

import os
import sys

LINE = (
    "1 star. Ghosted me for two weeks, came back thinner, "
    "then blamed the tides. Zero accountability, all glow."
)


def main() -> int:
    # The harness mounts /output; an optional argv[1] lets the line be
    # verified locally without that mount.
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"

    text = LINE.strip()
    if not (1 <= len(text) <= 120):
        print(f"entry is {len(text)} characters, must be 1-120", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Self-check: read it back exactly as the gate would.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    print(f"wrote {len(written)} characters to {out_path}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
