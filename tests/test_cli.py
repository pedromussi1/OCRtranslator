"""CLI argument parsing (no OCR, no model)."""

from main import build_parser


def test_defaults():
    args = build_parser().parse_args(["page.jpg"])
    assert args.image == "page.jpg"
    assert args.to_lang == "en"
    assert args.from_lang is None


def test_explicit_langs():
    args = build_parser().parse_args(["page.jpg", "--to", "pt-br", "--from", "en"])
    assert args.to_lang == "pt-br"
    assert args.from_lang == "en"
