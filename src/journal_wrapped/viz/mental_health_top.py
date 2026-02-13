"""Top 10 mental health conditions horizontal bar chart."""

import matplotlib.pyplot as plt

from journal_wrapped.viz.style import (
    BAR_COLOR, TEXT_COLOR, setup_style, save_figure, load_json, parse_viz_args,
)

DEFAULT_INPUT = "out/llama/mental_health_*_normalized.json"


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    health_map = data["mental_health_map"]

    counts = {cond: len(entries) for cond, entries in health_map.items()}
    sorted_conds = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

    names = [c[0] for c in reversed(sorted_conds)]
    values = [c[1] for c in reversed(sorted_conds)]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(names, values, color=BAR_COLOR, height=0.65)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.8, bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center", ha="left", fontsize=10, color=TEXT_COLOR,
        )

    ax.set_title("Most mentioned mental health conditions")
    ax.set_xlim(0, max(values) * 1.12)
    ax.xaxis.set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    save_figure(fig, "mental_health_top")


if __name__ == "__main__":
    main()
