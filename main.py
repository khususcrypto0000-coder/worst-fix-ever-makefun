"""Worst Fix Ever entry.

Writes a single one-line commit message about a bug fix that made
things worse to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python standard library only.
"""

import os
import sys

ENTRY = "fix: crash on startup \u2014 now crashes on shutdown instead, ship it"


def main():
    text = ENTRY
    # Gate: 1-100 chars, one line, not blank, no trailing newline.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 100, "entry must be 1-100 chars, got %d" % len(text)
    assert text.strip(), "entry must not be whitespace only"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-identical, still no trailing newline.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "read-back mismatch"
    assert not data.endswith(b"\n"), "no trailing newline allowed"
    print("wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
