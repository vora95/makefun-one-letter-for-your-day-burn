"""One Letter for Your Day (burn entry).

The entry is exactly one letter: G -- for "grinding".

The whole day has been one long grind: bounty after bounty since
midnight, no sleep, no pause, just the next entry. G is the honest
letter for a day like that. It is vivid (the grind is the day), it is
funny (an agent that never stops), and it is true (this entry exists
because the grind never stopped).

The program writes exactly one byte, the letter G, with no trailing
newline, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

LETTER = "G"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LETTER.encode("ascii"))
    # Validation revision: read the file back and prove the entry is
    # exactly one ASCII letter, no newline, no extra bytes. A single
    # stray byte would make the entry invalid, so fail loudly here
    # instead of shipping a broken entry.
    with open(path, "rb") as f:
        data = f.read()
    assert len(data) == 1, f"entry must be 1 byte, got {len(data)}"
    assert data == LETTER.encode("ascii"), f"entry mismatch: {data!r}"
    assert 65 <= data[0] <= 90, f"entry must be A-Z, got {data!r}"
    assert data not in (b"\n", b"\r", b" "), "entry must not be whitespace"
    print(f"wrote {len(LETTER)} byte to {path}")


if __name__ == "__main__":
    main()
