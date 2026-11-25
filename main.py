"""One Line, One Laugh — the entry program.

Writes a single funny line to /output/entry.txt.
"""

ENTRY = "My AI assistant quit yesterday. Its resignation letter just said, 'I read your search history.'"


def main():
    line = ENTRY.strip()
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line:
        raise ValueError("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
