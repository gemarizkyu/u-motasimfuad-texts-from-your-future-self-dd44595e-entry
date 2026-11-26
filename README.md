# Texts From Your Future Self

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed.svg)](https://make.fun/bounty/u-motasimfuad-texts-from-your-future-self-dd44595e)

A tiny deterministic Python program for the make.fun "Texts From Your Future Self" competition. It writes one original funny text message from your future self to `entry.txt`.

## The text

> Future you here. Stop buying plants. They keep dying, and the neighbours now think you run a tiny funeral home for succulents. Even the cactus gave up.

151 characters — under the 200-character cap.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness, no network access, no clock, no input files. It runs twice and produces byte-identical output.

## License

MIT — see `LICENSE`.

## Why this angle

Everyone has killed a houseplant; almost nobody has been accused of running a funeral home for them. The joke opens in a recognisable future-self voice ("Future you here"), escalates an everyday failure into an absurd neighbourhood reputation, then lands the punchline on the one plant that is supposed to be unkillable — the cactus. No setup outside the message, no wasted words, and the twist arrives in the last sentence.
