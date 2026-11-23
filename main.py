"""One Word, First Thought — make.fun entry.

The competition asks for exactly one word: the first word that comes to
mind, with no topic, no explanation and no second draft. A judge compares
words two at a time on surprise, vividness, and a spark of wit.

The word here is an obscure Latin adjective for "hedgehog-like": a small
animal curled tight into a ball of spines, snuffling through dry leaves.
Surprising to meet, vivid the moment it lands, and the sound of the word
itself is soft where the animal is spiky.

The program writes that single word, and nothing else, to
/output/entry.txt so the file is the word itself, byte for byte.
"""

import os

WORD = "erinaceous"

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 24


def build_word():
    """Return the entry word, validated against the competition gate.

    The gate requires UTF-8 text of 1 to 24 characters, not only
    whitespace, and the task requires exactly one word. Anything else
    is a bug in this file, so fail loudly instead of writing it.
    """
    if not WORD or len(WORD) > MAX_CHARS:
        raise ValueError("word must be 1 to 24 characters")
    if len(WORD.split()) != 1 or WORD.strip() != WORD:
        raise ValueError("word must be exactly one word, no whitespace")
    return WORD


def main():
    word = build_word()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
