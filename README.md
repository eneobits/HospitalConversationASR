# HospitalConversationASR

Fine-tuning and evaluation code for Korean clinical telephone conversation ASR based on Whisper large-v3-turbo.

## Overview

This repository contains the training scripts, evaluation scripts, and supporting documentation used in the study on automatic speech recognition (ASR) for Korean hospital conversation data. The project focuses on domain-specific fine-tuning of Whisper large-v3-turbo for clinical telemedicine-style speech and evaluates performance using word error rate (WER) and character error rate (CER).

## Related Manuscript

**Title:** Fine-Tuning Whisper large-v3-turbo for Korean Clinical Telephone Conversation ASR  
**Status:** Repository prepared for public release upon manuscript acceptance/publication.

Citation information will be updated after publication.

## Repository Contents

- Fine-tuning scripts for Whisper large-v3-turbo
- Evaluation scripts for WER and CER
- Inference scripts for transcription
- Configuration examples
- Documentation for environment setup and reproduction workflow

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
