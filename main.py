"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic:
the same line, byte for byte, on every run.
"""

import os

LINE = "Your future self is already debugging the shortcut you take today."


def main():
    if not 1 <= len(LINE) <= 120 or LINE.strip() == "" or "\n" in LINE:
        raise ValueError("entry line must be one non-empty line of 1-120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
