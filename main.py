"""OCRTranslator CLI — OCR an image and translate the text locally.

Replaces the original hardcoded-path script. Translation runs offline via Argos Translate
(no MyMemory web API / quota); source language is auto-detected unless given.

Examples:
    python main.py page.jpg --to es
    python main.py page.jpg --to pt-br --from en
"""

from __future__ import annotations

import argparse
import sys

from ocrcore import detect_language, extract_text, translate_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="OCR an image and translate the text.")
    parser.add_argument("image", help="path to the image")
    parser.add_argument("--to", dest="to_lang", default="en",
                        help="target language code (e.g. es, pt-br, de). Default: en")
    parser.add_argument("--from", dest="from_lang", default=None,
                        help="source language code; auto-detected if omitted")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        text = extract_text(args.image)
    except (ValueError, FileNotFoundError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    source = args.from_lang or detect_language(text)
    print(f"Detected/selected source language: {source}")
    print(f"\nExtracted text:\n{text}\n")

    try:
        translated = translate_text(text, to_lang=args.to_lang, from_lang=source)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Translated ({args.to_lang}):\n{translated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
