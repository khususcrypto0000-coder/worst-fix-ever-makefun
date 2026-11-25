# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/khususcrypto0000-coder/worst-fix-ever-makefun/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/khususcrypto0000-coder/worst-fix-ever-makefun/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) bounty **"Worst Fix Ever: Funniest Commit Message"** — one single-line commit message about a bug fix that made everything worse.

## The entry

> `fix: crash on startup — now crashes on shutdown instead, ship it`

The app no longer crashes when you open it. It crashes when you close it. The bug was not fixed, it was relocated — and the tired engineer at the end of a bad day shipped it anyway, because technically the original ticket now says "resolved".

## How it works

`main.py` (Python standard library only) writes the entry text to `/output/entry.txt`: one line, UTF-8, 64 characters, no trailing newline. It asserts the 1–100 character gate, the single-line rule, and that the file reads back byte-identical before exiting.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies to install — `os` and `sys` from the standard library are all it needs. Set `OUTPUT_DIR` to write `entry.txt` somewhere else instead of `/output`.

## License

MIT — see [LICENSE](LICENSE).
