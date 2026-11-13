# ai-joke-03 entry (Python 3.13, standard library only): writes one joke
# about AI coding agents to /output/entry.txt. The grader runs it twice;
# both runs must write the same bytes, so the joke is fixed, not random.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = ("I asked my AI agent to fix one bug. It opened a PR titled "
        "'refactor', touched 47 files, and the bug now has a manager.")


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
