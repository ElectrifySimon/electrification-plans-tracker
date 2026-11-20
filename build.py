#!/usr/bin/env python3
"""Encrypt src/data.json into data.enc.json for the static tracker.

Password comes from the env var TRACKER_PASSWORD, never from a file in the repo.
Format: {"v":1,"kdf":"PBKDF2-SHA256","iter":310000,"salt":b64,"iv":b64,"ct":b64}
"""
import base64
import json
import os
import pathlib
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "data.json"
OUT = ROOT / "data.enc.json"
ITER = 310_000


def b64(b: bytes) -> str:
    return base64.b64encode(b).decode()


def main() -> int:
    pw = os.environ.get("TRACKER_PASSWORD")
    if not pw or len(pw) < 8:
        print("TRACKER_PASSWORD missing or too short", file=sys.stderr)
        return 2
    payload = SRC.read_bytes()
    # validate JSON before encrypting
    json.loads(payload)
    salt = os.urandom(16)
    iv = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER)
    key = kdf.derive(pw.encode())
    ct = AESGCM(key).encrypt(iv, payload, b"electrification-tracker-v1")
    doc = {
        "v": 1,
        "kdf": "PBKDF2-SHA256",
        "iter": ITER,
        "salt": b64(salt),
        "iv": b64(iv),
        "ct": b64(ct),
    }
    OUT.write_text(json.dumps(doc, indent=2) + "\n")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(payload)} bytes plaintext)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
