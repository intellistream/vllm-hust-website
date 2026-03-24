#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = Path(__file__).resolve()

TEXT_EXTENSIONS = {
    ".html",
    ".css",
    ".js",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".yml",
    ".yaml",
    ".txt",
}

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

FORBIDDEN_PATTERNS = {
    "huggingface_hub.InferenceClient": "Do not use Hugging Face inference shortcuts in the website serving path.",
    "from huggingface_hub import InferenceClient": "Do not use Hugging Face inference shortcuts in the website serving path.",
    "api-inference.huggingface.co/models": "Do not call hosted Hugging Face inference endpoints from the website.",
    "InferenceClient(": "Do not instantiate Hugging Face inference clients in this repo.",
    "text_generation(": "Do not use text-generation shortcuts in the website serving path.",
    "chat_completion(": "Do not use hosted chat-completion shortcuts in the website serving path.",
}


def should_scan(path: Path) -> bool:
    if path.resolve() == SELF_PATH:
        return False
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False
    return path.suffix in TEXT_EXTENSIONS


def scan_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    violations: list[str] = []
    for needle, message in FORBIDDEN_PATTERNS.items():
        if needle in text:
            rel = path.relative_to(REPO_ROOT)
            violations.append(f"{rel}: {message} [{needle}]")
    return violations


def main() -> int:
    violations: list[str] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or not should_scan(path):
            continue
        violations.extend(scan_file(path))

    if violations:
        print("Architecture guard failed:", file=sys.stderr)
        for violation in violations:
            print(f"- {violation}", file=sys.stderr)
        return 1

    print("Architecture guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
