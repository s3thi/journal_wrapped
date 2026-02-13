"""Top 15 most-mentioned people horizontal bar chart."""

import json
from pathlib import Path

import matplotlib.pyplot as plt

from journal_wrapped.viz.style import (
    BAR_COLOR, TEXT_COLOR, setup_style, save_figure, load_json, parse_viz_args,
)

NAME_MAP_PATH = Path(__file__).resolve().parents[3] / "name_map.json"

DEFAULT_INPUT = "out/llama/people_*_normalized.json"

# Only people in this list will be included.
REAL_PEOPLE = { }


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    people_map = data["people_map"]

    # Filter to real people only (exclude Claude and fictional/author names)
    counts = {}
    for person, entries in people_map.items():
        if person in REAL_PEOPLE:
            counts[person] = len(entries)

    sorted_people = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:15]

    name_map = {}
    if NAME_MAP_PATH.exists():
        name_map = json.loads(NAME_MAP_PATH.read_text())

    names = [name_map.get(p[0], p[0]) for p in reversed(sorted_people)]
    values = [p[1] for p in reversed(sorted_people)]

    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.barh(names, values, color=BAR_COLOR, height=0.65)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + 0.5, bar.get_y() + bar.get_height() / 2,
            str(int(width)),
            va="center", ha="left", fontsize=10, color=TEXT_COLOR,
        )

    ax.set_title("Most mentioned people")
    ax.set_xlim(0, max(values) * 1.12)
    ax.xaxis.set_visible(False)
    ax.grid(axis="y", visible=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    save_figure(fig, "people_top")


if __name__ == "__main__":
    main()
