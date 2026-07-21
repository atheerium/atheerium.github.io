#!/usr/bin/env bash
# publish.sh - One-command article publish workflow
# Usage: bash scripts/publish.sh "Article title"
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

MSG="${1:-Publish new content}"

echo "=== 1. Regenerate INDEX.md ==="
python3 scripts/generate-index.py

echo ""
echo "=== 2. Build site ==="
pnpm build 2>&1 | tail -3

echo ""
echo "=== 3. Stage everything ==="
git add -A

if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

echo ""
echo "=== 4. Commit ==="
git commit -m "$MSG"

echo ""
echo "=== 5. Push ==="
git push

echo ""
echo "Done! Site deployed via GitHub Actions."
echo "Check: https://github.com/atheerium/atheerium.github.io/actions"
