"""Notable one-off social events -- styled list visualization."""

import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from journal_wrapped.viz.social_data import ONE_OFF_EVENTS
from journal_wrapped.viz.style import (
    COLORS, TEXT_COLOR, BACKGROUND, setup_style, save_figure, load_json,
    parse_viz_args,
)

NAME_MAP_PATH = Path(__file__).resolve().parents[3] / "name_map.json"

# Deduplicate events that differ only in casing.
MERGE = {}

DEFAULT_INPUT = "out/llama/social_*.json"


def _load_name_map():
    if NAME_MAP_PATH.exists():
        return json.loads(NAME_MAP_PATH.read_text())
    return {}


EXTRA_REPLACEMENTS = {}


def _replace_names(text, name_map):
    if text in EXTRA_REPLACEMENTS:
        return EXTRA_REPLACEMENTS[text]
    for real, alias in sorted(name_map.items(), key=lambda x: -len(x[0])):
        text = re.sub(re.escape(real), alias, text)
    return text


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    name_map = _load_name_map()

    seen = set()
    events = []
    for event_name in ONE_OFF_EVENTS:
        if event_name not in data:
            continue
        canonical = MERGE.get(event_name, event_name)
        if canonical in seen:
            continue
        seen.add(canonical)
        events.append(_replace_names(canonical, name_map))

    n = len(events)
    row_height = 0.55
    fig_height = max(4, n * row_height + 2)

    fig, ax = plt.subplots(figsize=(10, fig_height))
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, n - 0.5)
    ax.invert_yaxis()
    ax.axis("off")

    ax.set_title("Notable events in 2025", fontsize=16, fontweight="bold", pad=16)

    for i, event in enumerate(events):
        color = COLORS[i % len(COLORS)]

        marker = mpatches.FancyBboxPatch(
            (0.3, i - 0.18), 0.36, 0.36,
            boxstyle="round,pad=0.05",
            facecolor=color, edgecolor="none",
        )
        ax.add_patch(marker)

        ax.text(
            1.1, i, event,
            va="center", ha="left",
            fontsize=13, color=TEXT_COLOR,
        )

    save_figure(fig, "social_events")


if __name__ == "__main__":
    main()
