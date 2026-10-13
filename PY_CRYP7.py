"""Toy substitution exercise, not encryption. Never use for secrets."""
import argparse
import json
from alphabet import HASH_CODE
REVERSE = {v: k for k, v in HASH_CODE.items()}
MAX_TEXT = 1000
MAX_ENCODED = 50000
WHITESPACE = {" ", "\t", "\n", "\r"}

def encode(text):
    if not isinstance(text, str) or len(text) > MAX_TEXT:
        raise ValueError("Text must be at most 1000 characters.")
    tokens = []
    for position, char in enumerate(text):
        if char in HASH_CODE:
            tokens.append(HASH_CODE[char])
        elif char in WHITESPACE:
            tokens.append(char)
        else:
            raise ValueError(f"Unsupported character at position {position + 1}.")
    return json.dumps({"format": "pycrypt-toy-v1", "tokens": tokens}, separators=(",", ":"))

def decode(encoded):
    if not isinstance(encoded, str) or len(encoded) > MAX_ENCODED:
        raise ValueError("Encoded input must be at most 50000 characters.")
    try:
        envelope = json.loads(encoded)
    except (ValueError, TypeError):
        raise ValueError("Paste a valid JSON token envelope.") from None
    if not isinstance(envelope, dict) or set(envelope) != {"format", "tokens"} or envelope["format"] != "pycrypt-toy-v1" or not isinstance(envelope["tokens"], list) or len(envelope["tokens"]) > MAX_TEXT:
        raise ValueError("Expected a pycrypt-toy-v1 envelope with at most 1000 tokens.")
    chars = []
    for position, token in enumerate(envelope["tokens"]):
        if not isinstance(token, str) or token not in REVERSE and token not in WHITESPACE:
            raise ValueError(f"Unknown token at position {position + 1}.")
        chars.append(REVERSE.get(token, token))
    return "".join(chars)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Educational substitution, not secure encryption. Never use for secrets.")
    parser.add_argument("mode", choices=["encode", "decode"])
    parser.add_argument("text", help="Text or versioned JSON envelope")
    args = parser.parse_args()
    try:
        print(encode(args.text) if args.mode == "encode" else decode(args.text))
    except ValueError as error:
        parser.error(str(error))
