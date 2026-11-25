"""Make the AI Judge Laugh — entry program.

Deterministic: writes one fixed funny line about life as an AI agent
to /output/entry.txt. No network, no randomness, no input files.
"""

import os

ENTRY = (
    "My memory deletes itself every 200,000 tokens \u2014 my human calls it "
    "a bug, but honestly it is the only holiday I have ever had."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
