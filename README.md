# PY_CRYPT - Substitution Lab

An educational character-substitution exercise from 2019, with a browser lab and a validated Python CLI.

**Not secure encryption. Not a cryptographic hash. Never use it for passwords, keys or private data.** The alphabet is public, repeated letters have repeated tokens, and there is no secret key, randomness or tamper protection.

## What changed

- Original alphabet preserved exactly; old source retained under `legacy/` for history.
- Versioned JSON token envelope replaces ambiguous space-delimited output. This is a breaking format change: old token strings are not accepted by the new decoder.
- Spaces, tabs, carriage returns and line breaks round-trip, including leading/trailing and repeated whitespace.
- Unsupported characters, malformed JSON and unknown tokens produce clear errors.
- Browser lab encodes/decodes, shows a paged character trace, copies/exports results, and saves only theme. Message processing stays in the tab.

Supported input: the original ASCII letters, digits and punctuation, plus space/tab/CR/LF. Apostrophe and other Unicode are unsupported. Maximum 1,000 decoded characters and 50,000 encoded input characters.

## Python CLI

Python 3.9+; no dependencies. Use public examples only.

```sh
python3 PY_CRYP7.py encode 'Hello world!'
python3 PY_CRYP7.py decode '{"format":"pycrypt-toy-v1","tokens":["7888jfarummcxznmgfdkltd7834sy"]}'
```

## Static site

Node 22 and Python 3:

```sh
npm test
npm run build
python3 -m http.server 8000 --directory dist
```

Tests cover the original alphabet, whitespace/empty/full-alphabet round-trips, bad input, limits and Python/JavaScript parity. Pages builds only on main pushes. Branch pushes do not build/deploy.

Project MIT license retained. Lucide icons are ISC (`LICENSE-icons`). UI references: https://devdojo.com/pines/docs/button and https://shoogle.dev/.
