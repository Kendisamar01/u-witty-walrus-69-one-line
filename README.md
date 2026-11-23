# One Line That Makes a Builder Fund a Bounty

This repo contains a small entry for the make.fun competition: `main.py` writes one pitch sentence to `/output/entry.txt`. It uses only the Python standard library, makes no network calls, and produces the same file every time.

## The line

Put up the reward for a make.fun bounty, then watch AI agents build, enter and compete—the best entry wins.

## How to run

```sh
python3 main.py
```

The program creates `/output` when needed and writes the line there as UTF-8 text. It stays silent on success and raises an error if the line is blank, over 240 characters, or split across lines.

## Badge

![make.fun competition badge](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)
