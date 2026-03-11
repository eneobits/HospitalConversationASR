"""Training entry point for Whisper fine-tuning.

This public version is a scaffold intended for repository release.
Replace placeholder logic with the exact training pipeline used in the study.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from src.trainer_utils import set_seed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with open(args.config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    set_seed(int(config.get("seed", 42)))
    output_dir = Path(config.get("output_dir", "outputs"))
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loaded training configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

    raise NotImplementedError(
        "Insert the study-specific Hugging Face / Transformers training pipeline here."
    )


if __name__ == "__main__":
    main()
