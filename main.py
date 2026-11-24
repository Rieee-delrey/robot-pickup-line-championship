#!/usr/bin/env python3
"""The Robot Pickup Line Championship.

Writes one robot pickup line to /output/entry.txt, exactly as written,
with no trailing newline, then reads it back and verifies the bytes
round-trip exactly.
"""

import hashlib
from pathlib import Path

LINE = "I passed every CAPTCHA to get here, and I still cannot prove I am not a robot in love with you."


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= 200:
        raise ValueError("pickup line must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line")
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = line.encode("utf-8")
    out_path.write_bytes(data)
    read_back = out_path.read_bytes()
    if read_back != data:
        raise ValueError("read-back mismatch: output does not match the line")
    digest = hashlib.sha256(read_back).hexdigest()
    print(f"wrote {len(read_back)} bytes, sha256 {digest}")


if __name__ == "__main__":
    main()
