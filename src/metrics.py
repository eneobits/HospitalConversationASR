"""Metric helpers for ASR evaluation."""

from __future__ import annotations

from jiwer import cer, wer


def compute_wer(references: list[str], predictions: list[str]) -> float:
    """Compute word error rate."""
    return wer(references, predictions)


def compute_cer(references: list[str], predictions: list[str]) -> float:
    """Compute character error rate."""
    return cer(references, predictions)
