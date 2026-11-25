#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note a smart fridge leaves for its owner.
Stdlib only, no network, fully deterministic.
"""

import os

NOTE = (
    "The door was open 47 seconds. The ice maker saw everything. "
    "The yogurt expired Tuesday and asked me to stop telling it about you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE + "\n")


if __name__ == "__main__":
    main()
