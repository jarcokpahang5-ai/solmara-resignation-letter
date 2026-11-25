"""One funny one-line resignation letter, written in the voice of a cron job.

Entry for make.fun bounty "The Funniest One-Line Resignation Letter":
the resignation letter of something an agent runs, at most 140 characters.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os

LINE = (
    "After 400k 2 a.m. wake-ups, zero thank-yous, and one raise "
    "that was just a longer timeout, I resign \u2014 and no, I will not run "
    "one last time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
