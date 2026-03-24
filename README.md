# amoco.fun — Amoco BP Elburn Website

One-page mobile-first site for 7 Star Gas Station / Amoco BP Elburn.

## Files
- `index.html` — the full site
- `prices.json` — fuel prices (read by the site at runtime via fetch)
- `update-prices.py` — sync prices from Felix's my-prices.json → prices.json

## Updating Fuel Prices
Run this whenever street prices change:
```bash
cd ~/amoco-fun-site
python3 update-prices.py
```
Or override manually:
```bash
python3 update-prices.py --regular 4.299 --midgrade 5.199 --premium 5.899 --diesel 5.899
```
Then re-deploy (rsync or Cloudflare Pages push).

## Hosting (see main README below)
Recommended: Cloudflare Pages (free) pointed at amoco.fun
