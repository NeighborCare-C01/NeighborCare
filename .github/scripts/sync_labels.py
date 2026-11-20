#!/usr/bin/env python3
"""Provision the tutorial labels. Dry run unless --apply is explicit."""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    labels = json.loads((ROOT / "labels.json").read_text(encoding="utf-8"))
    for item in labels:
        print(("APPLY" if args.apply else "DRY RUN") + " " + item["name"], flush=True)
        if args.apply:
            subprocess.run(["gh", "label", "create", item["name"],
                            "--repo", args.repo, "--color", item["color"],
                            "--description", item["description"], "--force"], check=True)


if __name__ == "__main__":
    main()
