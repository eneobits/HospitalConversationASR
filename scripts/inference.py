"""Inference script for single-audio transcription.

This public version is a scaffold intended for repository release.
Replace placeholder logic with the exact inference pipeline used in the study.
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_path", required=True)
    parser.add_argument("--checkpoint", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"Audio path: {args.audio_path}")
    print(f"Checkpoint: {args.checkpoint}")

    raise NotImplementedError(
        "Insert the study-specific inference workflow here for transcription."
    )


if __name__ == "__main__":
    main()
