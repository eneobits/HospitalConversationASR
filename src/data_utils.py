"""Utilities for loading and validating dataset manifests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, List, Dict


def load_manifest(path: str | Path) -> List[Dict[str, Any]]:
    """Load a JSON manifest file.

    Expected format: a list of dictionaries with at least
    `audio_filepath` and `transcript` keys.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Manifest must be a list of JSON objects.")
    return data


def validate_manifest(records: List[Dict[str, Any]]) -> None:
    """Validate required manifest fields."""
    required = {"audio_filepath", "transcript"}
    for idx, rec in enumerate(records):
        missing = required - set(rec)
        if missing:
            raise ValueError(f"Record {idx} is missing required keys: {missing}")
