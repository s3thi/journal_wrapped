"""Recurring communities horizontal bar chart."""

from collections import defaultdict

import matplotlib.pyplot as plt

from journal_wrapped.viz.social_data import RECURRING_GROUPS
from journal_wrapped.viz.style import (
    BAR_COLOR, TEXT_COLOR, setup_style, save_figure, load_json, parse_viz_args,
)

DEFAULT_INPUT = "out/llama/social_*.json"


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)

    community_counts = defaultdict(int)
    for event_name, info in data.items():
        if event_name in RECURRING_GROUPS:
            canonical = RECURRING_GROUPS[event_name]
            community_counts[canonical] += info["count"]

    sorted_communities = sorted(
        community_counts.items(), key=lambda x: x[1], reverse=True
    )

    names = [c[0] for c in reversed(sorted_communities)]
    values = [c[1] for c in reversed(sorted_communities)]

    fig, ax = plt.subplots(figsize=(10, max(4, len(names) * 0.9 + 2)))
    bars = ax.barh(names, values, color=BAR_COLOR, height=0.65)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.5, bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center", ha="left", fontsize=10, color=TEXT_COLOR,
        )

    ax.set_title("Recurring communities in 2025")
    ax.set_xlim(0, max(values) * 1.12)
    ax.xaxis.set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    save_figure(fig, "social_recurring")


if __name__ == "__main__":
    main()
