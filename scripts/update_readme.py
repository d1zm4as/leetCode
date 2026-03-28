#!/usr/bin/env python3
"""Update README stats based on repo contents."""
from __future__ import annotations

import os
import re
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
README_PATH = os.path.join(ROOT, "README.md")

EXCLUDE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}

EXT_MAP = {
    ".py": "Python",
    ".sql": "SQL",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".go": "Go",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".sh": "Bash",
}

SECTIONS = [
    "easy",
    "medium",
    "hard",
    "LeetCode75",
    "DataStructure",
    "Programming Skills",
    "Quests",
    "Top interview150",
    "Weekly Contest 490",
]


def collect_code_files() -> list[str]:
    files: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            if fname == ".DS_Store":
                continue
            path = os.path.join(dirpath, fname)
            if os.path.isfile(path):
                files.append(path)
    return files


def compute_stats(files: list[str]) -> tuple[int, Counter, dict[str, int]]:
    lang_counts: Counter = Counter()
    code_files: list[str] = []
    for path in files:
        ext = os.path.splitext(path)[1].lower()
        if ext in EXT_MAP:
            lang_counts[EXT_MAP[ext]] += 1
            code_files.append(path)

    section_counts = {section: 0 for section in SECTIONS}
    for path in code_files:
        rel = os.path.relpath(path, ROOT)
        top = rel.split(os.sep)[0]
        if top in section_counts:
            section_counts[top] += 1

    return len(code_files), lang_counts, section_counts


def replace_once(text: str, pattern: str, repl: str) -> str:
    new_text, count = re.subn(pattern, repl, text, flags=re.M)
    if count != 1:
        raise ValueError(f"Expected 1 match for pattern: {pattern}, got {count}")
    return new_text


def update_readme(total: int, lang_counts: Counter, section_counts: dict[str, int]) -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    text = replace_once(text, r"^- \d+ solution files\.$", f"- {total} solution files.")

    langs = sorted(lang_counts.items(), key=lambda kv: (-kv[1], kv[0]))
    lang_line = ", ".join([f"{count} {name}" for name, count in langs])
    text = replace_once(text, r"^- Languages: .*?$", f"- Languages: {lang_line}.")

    for section, count in section_counts.items():
        pattern = rf"^- `{re.escape(section)}` \(\d+ solutions\)$"
        repl = f"- `{section}` ({count} solutions)"
        text = replace_once(text, pattern, repl)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    files = collect_code_files()
    total, lang_counts, section_counts = compute_stats(files)
    update_readme(total, lang_counts, section_counts)


if __name__ == "__main__":
    main()
