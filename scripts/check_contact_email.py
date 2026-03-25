#!/usr/bin/env python3
"""Regression check for the obfuscated contact email in index.html."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX_HTML = ROOT / "index.html"
EXPECTED_EMAIL = "Bryangitau@yahoo.com"
EXPECTED_DOMAIN = "@yahoo.com"


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def main() -> None:
    content = INDEX_HTML.read_text(encoding="utf-8")

    encoded_match = re.search(r"const encodedEmail = \[([^\]]+)\];", content)
    if not encoded_match:
        fail("Could not find encodedEmail in index.html")

    key_match = re.search(r"const key = (\d+);", content)
    if not key_match:
        fail("Could not find decode key in index.html")

    try:
        encoded_values = [int(part.strip()) for part in encoded_match.group(1).split(",")]
    except ValueError as exc:
        fail(f"encodedEmail contains non-integer values: {exc}")

    key = int(key_match.group(1))
    decoded_email = "".join(chr(value ^ key) for value in encoded_values)

    # Keep this format check aligned with index.html:isValidContactEmail.
    email_match = re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", decoded_email)
    if not email_match:
        fail(f"Decoded email is not a valid format: {decoded_email!r}")

    if not decoded_email.lower().endswith(EXPECTED_DOMAIN):
        fail(f"Decoded email must end with {EXPECTED_DOMAIN}: {decoded_email!r}")

    if decoded_email != EXPECTED_EMAIL:
        fail(
            f"Decoded email does not match expected value. "
            f"Expected {EXPECTED_EMAIL!r}, got {decoded_email!r}"
        )

    print(f"[OK] Contact email decoded successfully: {decoded_email}")


if __name__ == "__main__":
    main()
