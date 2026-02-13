"""Hobbies by month stacked area chart (top 8 + Other)."""

import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

from journal_wrapped.viz.style import (
    COLORS, BACKGROUND, TEXT_COLOR, setup_style, save_figure, load_json,
    parse_date, parse_viz_args,
)

DEFAULT_INPUT = "out/llama/hobbies_*_normalized.json"
from journal_wrapped.viz.hobbies import EXCLUDE, MERGE

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    hobbies_map = data["hobbies_map"]

    # Apply merge and exclude, rebuilding the map with canonical names
    cleaned_map = defaultdict(list)
    for hobby, entries in hobbies_map.items():
        canonical = MERGE.get(hobby, hobby)
        if canonical in EXCLUDE:
            continue
        cleaned_map[canonical].extend(entries)

    # Count total per hobby to find top 8
    totals = {hobby: len(entries) for hobby, entries in cleaned_map.items()}
    top_hobbies = [h for h, _ in sorted(totals.items(), key=lambda x: x[1], reverse=True)[:8]]

    # Bucket by month for each hobby
    monthly = defaultdict(lambda: defaultdict(int))
    other_monthly = defaultdict(int)

    for hobby, entries in cleaned_map.items():
        for entry in entries:
            month_idx = parse_date(entry).month - 1  # 0-indexed
            if hobby in top_hobbies:
                monthly[hobby][month_idx] += 1
            else:
                other_monthly[month_idx] += 1

    # Build stacked data arrays
    x = np.arange(12)
    labels = top_hobbies + ["Other"]
    stacks = []
    for hobby in top_hobbies:
        stacks.append([monthly[hobby][m] for m in range(12)])
    stacks.append([other_monthly[m] for m in range(12)])

    colors = COLORS[:8] + ["#d0ccc4"]  # neutral gray for Other

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(x, *stacks, labels=labels, colors=colors, alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(MONTHS)
    ax.set_title("Hobbies through the year")
    ax.legend(loc="upper left", frameon=False, fontsize=9, ncol=3)
    ax.set_xlim(0, 11)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", visible=False)

    save_figure(fig, "hobbies_monthly")


if __name__ == "__main__":
    main()
