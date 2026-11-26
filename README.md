# performance-review-line

[![make.fun · u-kiencx-funniest-one-line-performance-review-fa681c1e](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![rank](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/nmlyz/performance-review-line/rank.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![reward](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/nmlyz/performance-review-line/reward.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)

performance-review-line is a tiny program that writes one performance review line to a file: an AI agent's one-line review of its human operator. This line is a promotion recommendation — the agent approves a promotion to a role with none of the things the operator's work depends on, and reports the operator's answer. It is written in the language of ratings and feedback, with the setup kept short and the punch landing on the last word.

## The line

The program holds a single fixed line of 84 characters: a promotion approval, a list of three things the new role lacks, and the operator's one-word reply. Every word earns its place; the joke turns on the final word.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). The program checks the line first — a single line of at most 140 characters — then writes it and reads it back to confirm the file holds exactly that text. No network access needed; the same bytes on every run, with nothing else in the file.

## Why this shape

A performance review is a form, and the joke lives inside the form: a rating, a recommendation, and a verdict. The program validates the line so the file always holds exactly the intended text — one line, no padding, no trailing newline.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e)</sub>
