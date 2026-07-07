<h1 align="center">OCR Translator (CLI)</h1>

<p align="center">
  <a href="https://www.youtube.com/watch?v=h8sp7vFeV7c"><img src="https://i.imgur.com/TCAQEac.gif" alt="YouTube Demonstration" width="800"></a>
</p>

<p align="center">Command-line tool that OCRs an image and translates the text into another language — <b>fully offline</b>, no API keys or quotas.</p>

CLI counterpart to
[OCRtranslator_Web](https://github.com/pedromussi1/OCRtranslator_Web); both share the same
`ocrcore` pipeline.

## What changed from the original

| Original | Now |
|---|---|
| Translated via the `translate` library's free **MyMemory** web API (daily character quota) | **Argos Translate** — local, offline neural MT (CTranslate2); no API key, no quota |
| Hardcoded image path + Tesseract path (`C:\Program Files\...`) | `argparse` CLI + cross-platform Tesseract discovery |
| Target language fixed in code | `--to` / `--from` flags with automatic source-language detection |
| No error handling, no deps file, no tests | Graceful errors, pinned `requirements.txt`, `pytest` suite |

## Usage

```bash
python -m venv .venv && .venv\Scripts\activate      # (source .venv/bin/activate on Unix)
pip install -r requirements.txt

python main.py page.jpg --to es
python main.py page.jpg --to pt-br --from en
```

Tesseract must be installed separately (`winget install tesseract`,
`brew install tesseract`, `apt install tesseract-ocr`). Argos downloads the requested
language model on first use, then runs offline.

## Layout

```
ocrcore/   shared pipeline (preprocess -> OCR -> detect -> translate)
main.py    CLI entry point
tests/     pytest suite
```

## Notes

- OCR defaults to **English source text**; install extra Tesseract language data to OCR
  other scripts.
- Not every language pair has a direct model; some route through English as a pivot.

## Tests

```bash
python -m pytest -q
```
