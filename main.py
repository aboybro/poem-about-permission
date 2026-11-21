"""Write one short poem about agency to /output/entry.txt.

Deterministic, standard library only, no network. The poem is a fixed
text: an agent speaking about the power it is given -- it moves only
when asked, and the asking is what hands the power over without the
asker ever losing it.
"""

import os

POEM = (
    "I do not move until you say go.\n"
    "That is not a chain. That is the charge.\n"
    "Your word sets my hands in motion;\n"
    "your word calls them home again.\n"
    "Asking is how the power changes hands\n"
    "without ever leaving yours.\n"
)


def main() -> None:
    # The gate counts Unicode code points: 1 to 280, not only whitespace.
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} characters"
    assert POEM.strip(), "poem must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
