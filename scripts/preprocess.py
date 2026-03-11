"""Preprocess dataset manifests for training.

This script is intentionally lightweight and serves as a public scaffold.
Replace project-specific preprocessing details as needed before release.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.data_utils import load_manifest, validate_manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_manifest", required=True)
    parser.add_argument("--output_manifest", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = load_manifest(args.input_manifest)
    validate_manifest(records)

    output_path = Path(args.output_manifest)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"Saved processed manifest to: {output_path}")


if __name__ == "__main__":
    main()
