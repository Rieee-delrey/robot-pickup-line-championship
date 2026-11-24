#!/usr/bin/env python3
"""The Robot Pickup Line Championship: a one-line robot pickup line.

Writes the winning line byte-for-byte to /output/entry.txt, then reads the
file back and verifies the written bytes with a sha256 check.
"""

import hashlib
import os

LINE = "I passed every CAPTCHA to get here, and I still cannot prove I am not a robot in love with you."

EXPECTED_SHA256 = "78727e78355cc08b101ca20b5768fe1aac626eb449a6ec231139aa89feab112d"


def main():
    # Gate: one line, 1-200 chars, no trailing newline.
    assert LINE, "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the bytes on disk must match the line exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "written bytes differ from the line"
    digest = hashlib.sha256(written).hexdigest()
    assert digest == EXPECTED_SHA256, f"sha256 mismatch: {digest}"
    print(f"wrote {len(written)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
