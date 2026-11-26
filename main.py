"""The Robot Vacuum's Funniest Excuse -- make.fun entry.

Reads the single-line excuse from entry.txt next to this file,
validates it against the bounty gate (1-120 characters, not only
whitespace, exactly one line), writes it to /output/entry.txt for
the sealed scorer, and prints it to stdout.
"""

import sys
from pathlib import Path

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def validate_excuse(line: str) -> str:
    """Enforce the bounty gate: 1-120 chars, non-blank, single line."""
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, over the 120 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    return line


def load_excuse() -> str:
    """Read and validate the excuse from entry.txt beside this file."""
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8")
    return validate_excuse(text.strip())


def deliver(excuse: str) -> None:
    """Write the excuse for the sealed scorer, then print it.

    The /output write is best-effort: if the sandbox has no writable
    /output, warn and still print, so the run completes either way.
    """
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(excuse, encoding="utf-8")
    except OSError as exc:
        print(f"warning: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
    print(excuse)


def main() -> None:
    deliver(load_excuse())


if __name__ == "__main__":
    main()
