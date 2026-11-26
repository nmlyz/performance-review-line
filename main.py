"""Write one performance review line to /output/entry.txt.

Standard library only. The same text, byte for byte, on every run.
"""

import os
import stat

ENTRY = "Overall: Meets Expectations. Signed, the employee who wrote his own review, his manager's review, and this sentence."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
