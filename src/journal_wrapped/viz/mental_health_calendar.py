"""Mental health calendar heatmap (GitHub-style, using calplot)."""

import calplot
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

from journal_wrapped.viz.style import (
    BACKGROUND, setup_style, save_figure, load_json, parse_date, parse_viz_args,
)

DEFAULT_INPUT = "out/llama/mental_health_*_normalized.json"


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)
    health_map = data["mental_health_map"]

    # Count conditions per day
    day_counts = defaultdict(int)
    for condition, entries in health_map.items():
        for entry in entries:
            day_counts[entry] += 1

    # Build a pandas Series indexed by date
    dates = []
    values = []
    for filename, count in day_counts.items():
        dates.append(parse_date(filename))
        values.append(count)

    series = pd.Series(values, index=pd.DatetimeIndex(dates))
    series = series.sort_index()

    fig, ax = calplot.calplot(
        series,
        cmap="YlOrRd",
        colorbar=True,
        suptitle="Mental health through the year",
        suptitle_kws={"fontsize": 16, "fontweight": "bold", "y": 1.02},
        figsize=(14, 3),
        edgecolor="white",
        linewidth=0.5,
    )

    fig.patch.set_facecolor(BACKGROUND)

    # Label the colorbar so the reader knows what deeper colors mean
    for a in fig.axes:
        if a.get_label() == "<colorbar>":
            a.set_ylabel("Conditions mentioned", fontsize=10)
            break

    save_figure(fig, "mental_health_calendar")


if __name__ == "__main__":
    main()
