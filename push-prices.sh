#!/bin/bash
# push-prices.sh — regenerate prices.json from my-prices.json and push to GitHub
# Called automatically whenever street prices are updated.

set -e

SITE_DIR="$HOME/amoco-fun-site"
cd "$SITE_DIR"

# Regenerate prices.json from Felix's market-watch data
python3 update-prices.py

# Check if prices.json actually changed
if git diff --quiet prices.json; then
  echo "prices.json unchanged — no push needed"
  exit 0
fi

# Commit and push
git add prices.json
git commit -m "Update fuel prices — $(date '+%B %-d, %Y')"
git push origin main

echo "✅ prices.json pushed to GitHub → Cloudflare Pages will auto-deploy"
