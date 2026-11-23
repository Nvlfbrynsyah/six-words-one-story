# Six Words, One Story

[![make.fun badge](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

Bounty: https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410

> She planted his ashes. Roses bloomed.

Six words carry an entire arc: grief, burial, and growth. A woman plants
the ashes of someone she has lost, an act of mourning that is also a planting.
Then the roses bloom — life answering loss, remembrance made living and
fragrant. The sentence moves from death to earth to flower in a single breath.

## Run

```sh
python3 main.py
```

By default the story is written to `/output/entry.txt`. Override the output
path with the `SIXWORDS_OUTPUT` environment variable:

```sh
SIXWORDS_OUTPUT=some/dir/entry.txt python3 main.py
```

Parent directories of the output path are created automatically. The program
self-checks that the story is exactly six words and exits non-zero otherwise.

## Verification

- 37 bytes
- 6 whitespace-separated words
- Two runs to different paths were byte-identical (sha256 below)

```text
cb27b865e4b704c5322d20bdea392e41704d2cda7e5de8e7bd3243bc67f4502e
```
