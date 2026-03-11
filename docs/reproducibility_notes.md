# Reproducibility Notes

## Purpose

This document summarizes practical considerations for reproducing the fine-tuning and evaluation pipeline.

## Factors Affecting Reproducibility

Exact reproduction may depend on:

- access to the same dataset version
- identical train/validation/test split definitions
- package versions
- GPU and CUDA environment
- random seed settings
- checkpoint selection criteria
- decoding and normalization settings

## Recommended Practices

- Use the exact dependency versions listed in the repository.
- Fix random seeds where possible.
- Preserve the original evaluation split.
- Use the same text normalization rules for WER/CER.
- Record hardware and software environment details.

## Scope

This repository is intended to support methodological transparency and approximate reproducibility of the fine-tuning workflow. Exact replication may not always be possible when dataset access conditions or runtime environments differ.
