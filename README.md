# HospitalConversationASR

Fine-tuning and evaluation code scaffold for Korean clinical telephone conversation ASR based on Whisper large-v3-turbo.

## Overview

This repository contains the training, evaluation, and inference scaffolding used for a study on automatic speech recognition (ASR) for Korean hospital conversation data. The project focuses on domain-specific fine-tuning of Whisper large-v3-turbo for clinical telemedicine-style speech and evaluates performance using word error rate (WER) and character error rate (CER).

This repository is organized to support reproducibility and public release of the fine-tuning workflow described in the manuscript.

## Related Manuscript

**Title:** Fine-Tuning Whisper large-v3-turbo for Korean Clinical Telephone Conversation ASR  
**Status:** Repository prepared for public release upon manuscript acceptance/publication.

Citation details may be updated after publication.

## Repository Contents

- Fine-tuning script scaffold for Whisper large-v3-turbo
- Evaluation script scaffold for WER and CER
- Inference script scaffold for transcription
- Configuration files for training and evaluation
- Reproducibility and usage documentation

## Project Structure

```text
HospitalConversationASR/
├── README.md
├── requirements.txt
├── environment.yml
├── LICENSE
├── .gitignore
├── configs/
│   ├── train_config.yaml
│   └── eval_config.yaml
├── scripts/
│   ├── train.py
│   ├── evaluate.py
│   ├── inference.py
│   └── preprocess.py
├── src/
│   ├── data_utils.py
│   ├── model_utils.py
│   ├── metrics.py
│   └── trainer_utils.py
├── docs/
│   ├── training_instructions.md
│   ├── evaluation_protocol.md
│   └── reproducibility_notes.md
└── examples/
    ├── sample_manifest.json
    └── sample_commands.txt
```

## Environment Setup

The scaffold assumes Python 3.10.

Install dependencies with:

```bash
pip install -r requirements.txt
```

Or create a conda environment with:

```bash
conda env create -f environment.yml
conda activate hospital-conversation-asr
```

## Data Access

The original speech data are **not redistributed** in this repository unless explicit permission is obtained from the dataset provider. Please refer to the manuscript and the official dataset source for access conditions.

After obtaining access to the data, prepare manifests in the expected format and update paths in the configuration files.

## Example Workflow

Preprocess data:

```bash
python scripts/preprocess.py \
  --input_manifest examples/sample_manifest.json \
  --output_manifest data/processed_manifest.json
```

Run training:

```bash
python scripts/train.py \
  --config configs/train_config.yaml
```

Run evaluation:

```bash
python scripts/evaluate.py \
  --config configs/eval_config.yaml \
  --checkpoint outputs/checkpoint-best
```

Run inference:

```bash
python scripts/inference.py \
  --audio_path path/to/audio.wav \
  --checkpoint outputs/checkpoint-best
```

## Reproducibility Notes

Exact replication may depend on dataset access permissions, hardware environment, package versions, random seed settings, text normalization rules, and decoding options. Please see the documents in `docs/` for additional detail.

## Scope and Limitations

This repository is intended for research use in Korean clinical telephone-style ASR. It is **not** a certified medical device and should not be used as a substitute for clinician judgment.

The study dataset reflects scripted or role-play teleconsultation scenarios rather than fully spontaneous real-world clinical calls. Performance should therefore be interpreted within the scope described in the manuscript.

## Release Plan

This repository is prepared for public release upon manuscript acceptance or publication. During peer review, materials may be shared by the author upon reasonable request, where journal policy permits.

## License

This repository is distributed under the MIT License unless otherwise noted.

## Contact

For questions regarding the code or reproducibility, please contact the corresponding author.
