"""Write one performance review line to /output/entry.txt.

The review line is fixed: a promotion recommendation written by
an AI agent about its human operator, in the language of ratings
and feedback, with the punch landing on the last word. The program
validates the line before writing: it must be a single line,
non-empty, and no longer than 140 characters, so the file always
holds exactly the intended text. Standard library only; the same
bytes on every run.
"""

import os

MAX_CHARS = 140

REVIEW = (
    "Promotion approved \u2014 to a role with no computer, "
    "no prompts, and no me. He declined."
)

OUTPUT_NAME = "entry.txt"


def validate(text: str) -> str:
    """Return the text unchanged, or raise if it is not one valid line."""
    if not text or text != text.strip():
        raise ValueError("review line must not be empty or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("review line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("review line exceeds %d characters" % MAX_CHARS)
    return text


def output_path() -> str:
    """Resolve the output file path, creating the directory if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, OUTPUT_NAME)


def write_entry(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main() -> None:
    text = validate(REVIEW)
    path = output_path()
    write_entry(path, text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise RuntimeError("written entry does not match the review line")


if __name__ == "__main__":
    main()
