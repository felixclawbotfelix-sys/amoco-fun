#!/usr/bin/env python3
"""
update-prices.py — sync street prices from my-prices.json → prices.json
Run this whenever you update street prices in the market-watch skill.

Usage:
  python3 update-prices.py
  python3 update-prices.py --regular 4.299 --midgrade 5.199 --premium 5.899 --diesel 5.899
"""

import json
import os
import sys
import argparse
from datetime import datetime

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
MY_PRICES = os.path.expanduser("~/.openclaw/workspace/skills/market-watch/data/my-prices.json")
PRICES_JSON = os.path.join(SITE_DIR, "prices.json")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--regular",  type=float)
    parser.add_argument("--midgrade", type=float)
    parser.add_argument("--premium",  type=float)
    parser.add_argument("--diesel",   type=float)
    args = parser.parse_args()

    # Start from my-prices.json if it exists
    if os.path.exists(MY_PRICES):
        with open(MY_PRICES) as f:
            src = json.load(f)
        prices = src.get("prices", {})
        out = {
            "regular":  prices.get("regular",  0),
            "midgrade": prices.get("midgrade", 0),
            "premium":  prices.get("premium",  0),
            "diesel":   prices.get("diesel",   0),
        }
    else:
        # Load existing prices.json
        with open(PRICES_JSON) as f:
            out = json.load(f)

    # Override with CLI args if provided
    if args.regular:  out["regular"]  = args.regular
    if args.midgrade: out["midgrade"] = args.midgrade
    if args.premium:  out["premium"]  = args.premium
    if args.diesel:   out["diesel"]   = args.diesel

    # Format updated date
    out["updated"] = datetime.now().strftime("%B %-d, %Y")

    with open(PRICES_JSON, "w") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    print(f"✅ prices.json updated:")
    print(f"   Regular:  ${out['regular']:.3f}")
    print(f"   Midgrade: ${out['midgrade']:.3f}")
    print(f"   Premium:  ${out['premium']:.3f}")
    print(f"   Diesel:   ${out['diesel']:.3f}")
    print(f"   Updated:  {out['updated']}")


if __name__ == "__main__":
    main()
