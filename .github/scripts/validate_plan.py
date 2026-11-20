#!/usr/bin/env python3
"""Fail closed unless Copilot returned exactly one bounded planning comment."""
import argparse
from pathlib import Path
import re

HEADER = "## Piano proposto dal Pianificatore AI"
ENDING = "In attesa di approvazione esplicita del TM. Nessuna modifica è stata effettuata."


def validate(text: str) -> str:
    body = text.strip()
    if not body.startswith(HEADER + "\n"):
        raise ValueError("Planning response has missing or incorrect heading")
    if not body.endswith(ENDING):
        raise ValueError("Planning response has missing or incorrect ending")
    if len(body) < 300 or len(body) > 12000:
        raise ValueError("Planning response outside 300-12000 character bounds")
    if re.search(r"(?i)(github_pat_|ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9_]+", body):
        raise ValueError("Possible credential-like content in response")
    for item in ("Ambito", "File", "Verific", "Risch"):
        if item.lower() not in body.lower():
            raise ValueError("Missing required planning topic: " + item)
    return body + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    body = validate(args.raw.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body, encoding="utf-8")
    print("Output conforms to the one-comment contract (" + str(len(body)) + " chars).")


if __name__ == "__main__":
    main()
