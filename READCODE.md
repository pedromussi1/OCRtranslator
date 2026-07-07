# Code Breakdown

OCR Translator (CLI) reads text from an image and translates it — **fully offline** — from
the command line. It shares the `ocrcore/` package with
[OCRtranslator_Web](https://github.com/pedromussi1/OCRtranslator_Web); `main.py` is a thin
argparse front-end.

## Pipeline

```
image ─▶ preprocess (OpenCV) ─▶ OCR (Tesseract) ─▶ detect language ─▶ translate (Argos)
```

## `ocrcore/` package
- **`preprocess.py`** — configurable OpenCV pipeline (upscale, denoise, threshold, deskew).
- **`ocr.py`** — Tesseract wrapper with cross-platform binary discovery; cleans the OCR text
  (rejoins hyphenated line breaks) while keeping punctuation/case.
- **`translate.py`** — **Argos Translate** (local, offline neural MT), replacing the original
  `translate`/MyMemory web API (daily quota). Auto-detects the source language, normalizes
  language codes, downloads a language package once then runs offline, and falls back to an
  **English pivot** for pairs without a direct model.

## `main.py`
Parses `--to` / `--from` (source auto-detected if omitted), runs `extract_text` →
`translate_text`, and prints the detected source language, the OCR text, and the translation.
Errors are reported cleanly with a non-zero exit code.

## Tests
`tests/` covers the text cleaning, language-code normalization, the no-op same-language path,
and CLI argument parsing.
