from pathlib import Path

# Print the office joke from entry.txt (path resolved via this file).
print(Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip())
