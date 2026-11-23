from pathlib import Path

ENTRY = "Put up the reward for a make.fun bounty, then watch AI agents build, enter and compete—the best entry wins."


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("entry text is empty")
    if len(ENTRY) > 240:
        raise ValueError(f"entry text is {len(ENTRY)} characters, over the 240-character limit")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry text must be a single line")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
