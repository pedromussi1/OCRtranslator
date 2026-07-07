# Changelog

All notable changes to this project are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-07-06

Complete rewrite: from a hardcoded-path script into a local, offline translation CLI.

### Added
- `ocrcore/` pipeline (shared with OCRtranslator_Web): preprocess → OCR → detect → translate.
- **Argos Translate** local, offline neural machine translation — no API key, no quota.
- `argparse` CLI with `--to` / `--from`; automatic source-language detection.
- English-pivot fallback for language pairs without a direct model.
- `pytest` suite (8 tests), pinned `requirements.txt`.

### Fixed
- Replaced the `translate` / MyMemory web API (daily character quota) with local translation.
- Hardcoded image path and Tesseract path → CLI arguments + cross-platform discovery.

### Changed
- README rewritten to document the offline CLI and its relationship to the web repo.

[2.0.0]: https://github.com/pedromussi1/OCRTranslator/releases/tag/v2.0.0
