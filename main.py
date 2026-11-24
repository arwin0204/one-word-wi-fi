"""One Word for Your Wi-Fi — make.fun bounty entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word: "Houdini".

Why this word: home Wi-Fi behaves like the great escape artist.
It is there one second and gone the next — mid-call, mid-download,
right when you need it most — then it reappears as if nothing
happened. No explanation, no apology. It is funny at once, true to
how Wi-Fi actually behaves at home, and it is not one of the words
everyone reaches for ("slow", "buffering", "laggy"). Any reader gets
the joke instantly: Houdini = the master of disappearing acts.
"""

import os

ENTRY = "Houdini"


def validate(word: str) -> None:
    """Self-check against the competition gate: 1 word, 1-20 chars."""
    if not (1 <= len(word) <= 20):
        raise ValueError(f"entry must be 1-20 characters, got {len(word)}")
    if len(word.split()) != 1 or not word.strip():
        raise ValueError("entry must be a single non-blank word")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
