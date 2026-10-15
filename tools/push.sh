#!/bin/sh
# Usage: sh tools/push.sh "message"   — commits everything and pushes to GitHub main
cd "$(dirname "$0")/.." || exit 1
git add -A && git commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HR4PJsHtTwThAuZv5A9tPi" || exit 1
git fetch -q origin main && git rebase -q origin/main && git push -q origin HEAD:main && git log --oneline -1
