#!/usr/bin/env python3
import hashlib
import sys

def sha256_from_string(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sha256_string.py <string>")
        sys.exit(1)

    input_text = sys.argv[1]
    print(sha256_from_string(input_text))
