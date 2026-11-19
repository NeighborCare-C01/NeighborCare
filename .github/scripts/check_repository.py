#!/usr/bin/env python3
"""Controlla i collegamenti locali Markdown senza dipendenze esterne.

Non controlla URL remoti o anchor; non segue link fuori dal repository.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {".git", "node_modules", "dist", "build", ".next", "target", ".venv"}
LINK = re.compile(r'!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\'][^"\']*["\'])?\s*\)')
REFERENCE = re.compile(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', re.MULTILINE)
FENCES = re.compile(r'^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', re.MULTILINE | re.DOTALL)


def candidate_urls(text):
    text = FENCES.sub("", text)
    for regex in (LINK, REFERENCE):
        for match in regex.finditer(text):
            yield match.group(1).strip("<>")


def check_file(md_path):
    errors = []
    body = md_path.read_text(encoding="utf-8")
    for url in candidate_urls(body):
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or url.startswith(("/", "#", "//")):
            continue
        target_name = unquote(parsed.path)
        if not target_name:
            continue
        target = (md_path.parent / target_name).resolve()
        if not target.is_relative_to(ROOT):
            errors.append(f"{md_path.relative_to(ROOT)}: link fuori dal repository: {url}")
        elif not target.exists():
            errors.append(f"{md_path.relative_to(ROOT)}: file non trovato: {url}")
    return errors


def main():
    markdown = sorted(p for p in ROOT.rglob("*.md")
                      if not set(p.relative_to(ROOT).parts) & EXCLUDED)
    errors = [error for path in markdown for error in check_file(path)]
    for error in errors:
        print("ERRORE:", error, file=sys.stderr)
    print(f"Controllati {len(markdown)} file Markdown; errori: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
