#!/usr/bin/env python3
"""Per-arm sample size for a two-proportion A/B test (two-sided, normal approximation).

Usage:
  sample_size.py BASELINE RELATIVE_LIFT [--alpha 0.05] [--power 0.8] [--monthly-visitors N]

  BASELINE        baseline conversion rate, e.g. 0.03 or 3% (values > 1 are read as percent)
  RELATIVE_LIFT   smallest relative lift worth detecting, e.g. 0.10 or 10%
"""
import argparse
import math
import sys
from statistics import NormalDist


def parse_rate(text):
    v = float(text.rstrip("%"))
    return v / 100 if text.endswith("%") or v > 1 else v


def sample_size_per_arm(p1, relative_lift, alpha=0.05, power=0.8):
    p2 = p1 * (1 + relative_lift)
    if not (0 < p1 < 1 and 0 < p2 < 1):
        raise ValueError("baseline and lifted rate must be between 0 and 1")
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (z_a * math.sqrt(2 * p_bar * (1 - p_bar))
           + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2), p2


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("baseline")
    ap.add_argument("lift")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.8)
    ap.add_argument("--monthly-visitors", type=float, help="visitors/month reaching the page, for duration estimate")
    a = ap.parse_args()

    p1 = parse_rate(a.baseline)
    lift = parse_rate(a.lift)
    n, p2 = sample_size_per_arm(p1, lift, a.alpha, a.power)

    print(f"baseline {p1:.2%} -> {p2:.2%} (relative lift {lift:.0%}), alpha {a.alpha}, power {a.power}")
    print(f"visitors per arm: {n:,}   total (2 arms): {2 * n:,}")
    print(f"conversions per arm at baseline: ~{math.ceil(n * p1):,}")
    if a.monthly_visitors:
        weeks = 2 * n / a.monthly_visitors * 52 / 12
        print(f"estimated duration at {a.monthly_visitors:,.0f} visitors/month: ~{weeks:.1f} weeks "
              f"(round up to whole weeks; run at least 2)")
        if weeks > 6:
            print("WARNING: over ~6 weeks. Consider a bigger change, a higher-volume metric, or shipping without a test.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        sys.exit(f"error: {e}")
