# Training Instructions

## Overview

This document describes the basic workflow used to fine-tune Whisper large-v3-turbo for Korean clinical telephone conversation ASR.

## Requirements

- Python 3.10
- CUDA-compatible GPU environment
- Dependencies listed in `requirements.txt` or `environment.yml`

## Data Preparation

Prepare a dataset manifest with the following fields:

- `audio_filepath`
- `transcript`
- `speaker_role` (optional if available)
- `split` (train / validation / test)

Example entry:

```json
{
  "audio_filepath": "/path/to/audio.wav",
  "transcript": "example transcript",
  "speaker_role": "patient",
  "split": "train"
}
```

## Preprocessing

```bash
python scripts/preprocess.py \
  --input_manifest examples/sample_manifest.json \
  --output_manifest data/processed_manifest.json
```

## Training

```bash
python scripts/train.py \
  --config configs/train_config.yaml
```

## Evaluation

```bash
python scripts/evaluate.py \
  --config configs/eval_config.yaml \
  --checkpoint outputs/checkpoint-best
```

## Notes

Exact numerical reproduction may vary depending on hardware environment, package version, data version, and random initialization. Please consult `docs/reproducibility_notes.md` for additional details.
