"""One Word, First Thought — make.fun entry.

The competition asks for a single word: the very first thought that
surfaces, with no explanation attached. This program writes exactly
that one word to the output file and nothing else.

The word is "erinaceous", a Latin-derived adjective meaning "like a
hedgehog". A hedgehog is a small animal that curls into a spiky ball
and snuffles through dry leaves — an image that lands instantly, yet
the word itself sounds soft and rolling, almost gentle, which is the
opposite of what the animal is. That surprise is why it sticks: it is
vivid, uncommon, and pleasant to say out loud.
"""

import os

WORD = "erinaceous"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 24


def build_word():
    """Return the single entry word, validated as exactly one word."""
    if not WORD or len(WORD) > MAX_CHARS:
        raise ValueError("WORD must be non-empty and at most MAX_CHARS long")
    if any(char.isspace() for char in WORD):
        raise ValueError("WORD must be exactly one word with no whitespace")
    return WORD


def main():
    """Write the word, and only the word, to the output file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(build_word())


if __name__ == "__main__":
    main()
