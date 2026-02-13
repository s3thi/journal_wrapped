"""Top 15 hobbies horizontal bar chart."""

from collections import defaultdict

import matplotlib.pyplot as plt

from journal_wrapped.viz.style import (
    BAR_COLOR, COLORS, TEXT_COLOR, setup_style, save_figure, load_json,
    parse_viz_args,
)

DEFAULT_INPUT = "out/llama/hobbies_*_normalized.json"

# Hobbies to drop from the chart entirely.
EXCLUDE = {"Gardening", "Photography", "Playing Guitar"}

# Merge aliases into a canonical name: {alias: canonical}.
# Entries for all aliases are combined under the canonical name.
MERGE = {
    "Writing Fiction": "Writing",
    "Coding": "Programming",
    "Software Development": "Programming"
}


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    hobbies_map = data["hobbies_map"]

    counts = defaultdict(int)
    for hobby, entries in hobbies_map.items():
        canonical = MERGE.get(hobby, hobby)
        if canonical in EXCLUDE:
            continue
        counts[canonical] += len(entries)
    counts = dict(counts)
    sorted_hobbies = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:15]

    # Reverse so the highest is at the top of the horizontal bar chart
    names = [h[0] for h in reversed(sorted_hobbies)]
    values = [h[1] for h in reversed(sorted_hobbies)]

    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(names, values, color=BAR_COLOR, height=0.65)

    # Value labels at the end of each bar
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.8, bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center", ha="left", fontsize=10, color=TEXT_COLOR,
        )

    ax.set_title("Most mentioned hobbies")
    ax.set_xlim(0, max(values) * 1.12)
    ax.xaxis.set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    save_figure(fig, "hobbies_top")


if __name__ == "__main__":
    main()
