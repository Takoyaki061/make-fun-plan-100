#!/usr/bin/env python3
"""Write the chosen plan text to /output/entry.txt (stdlib only)."""

import os

TEXT = (
    "Day 1: scrape and verify 500 hiring-manager emails for recruiting "
    "agencies, then email 200 a free 20-lead sample. Sell the full pack "
    "at $79, fresh lists weekly. The sample proves quality before anyone "
    "pays, and lists cost near zero to remake. Most likely $400-800 by "
    "day 30."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
