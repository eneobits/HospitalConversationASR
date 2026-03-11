# Evaluation Protocol

## Primary Metrics

The primary evaluation metrics are:

- Word Error Rate (WER)
- Character Error Rate (CER)

## General Procedure

1. Load the fine-tuned checkpoint.
2. Run transcription on the held-out evaluation split.
3. Apply the same text normalization rules used in the manuscript.
4. Compute WER and CER using consistent reference-prediction alignment.

## Recommended Reporting

- Report overall WER and CER.
- Report results by speaker role if available.
- Document normalization rules and decoding settings.
- Avoid direct subgroup fairness claims unless the dataset is designed for balanced subgroup evaluation.
