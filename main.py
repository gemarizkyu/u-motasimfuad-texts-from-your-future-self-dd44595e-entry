"""Write one funny text message from your future self to entry.txt.

Deterministic: the same text, byte for byte, on every run.
No randomness, no network, no clock, no model calls.
"""

import os

TEXT = (
    "Future you here. Stop buying plants. They keep dying, and the "
    "neighbours now think you run a tiny funeral home for succulents. "
    "Even the cactus gave up."
)


def main():
    assert 1 <= len(TEXT) <= 199, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
