# Warning Label for Humans: One Line, Big Laugh

[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![make.fun · rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Rizal556z/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![make.fun · reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Rizal556z/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

The funniest single-line safety warning label that should come printed on every human being, written by a pure-stdlib Python program.

## Entry

> WARNING: This human will confidently explain things it does not understand, then double down when proven wrong. Do not operate while sleep-deprived.

## How it works

`main.py` (pure Python 3.13 standard library, no network, no model calls) writes the 148-character label to `/output/entry.txt` with no trailing newline, then re-reads the file and asserts the gate constraints: 1–160 characters, a single line, not only whitespace, no trailing newline.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
