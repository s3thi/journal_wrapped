"""Media top lists -- grouped horizontal bar chart by category."""

from collections import defaultdict

import matplotlib.pyplot as plt

from journal_wrapped.viz.style import (
    COLORS, TEXT_COLOR, setup_style, save_figure, load_json, parse_viz_args,
)

DEFAULT_INPUT = "out/llama/media_*.json"

# Manual categorization of media items.
# Keys map to titles as they appear in the JSON (or groups of duplicates).
# Values are category names.

CATEGORIES = {
    # Books
    "The Secret History": "Books",
    "*The Secret History*": "Books",
    "All About Love": "Books",
    "The Lost Estate": "Books",
    "*The Lost Estate*": "Books",
    "Bunny": "Books",
    "Gormenghast": "Books",
    "A Memory Called Empire": "Books",
    "The Traitor Baru Cormorant": "Books",
    "Baru": "Books",
    "Manderley Forever": "Books",
    "A System for Writing": "Books",
    "Learning to Work": "Books",
    "*Learning to Work*": "Books",
    "Gentle Writing Advice": "Books",
    "*Gentle Writing Advice*": "Books",
    "The War of Art": "Books",
    "*War of Art*": "Books",
    "Upstream": "Books",
    "Silver Nitrate": "Books",
    "*Silver Nitrate*": "Books",
    "Nona the Ninth": "Books",
    "Fingersmith": "Books",
    "Our Wives Under the Sea": "Books",
    "Amusing Ourselves to Death": "Books",
    "The Broken Sword": "Books",
    "Staying Human": "Books",
    "The Big Questions": "Books",
    "Of Power and Time": "Books",
    "The Epic of Gilgamesh": "Books",
    "*Buttercream*": "Books",
    "*The Year's Best Software Writing*": "Books",

    # TV Shows
    "The Bear": "TV Shows",
    "*The Bear*": "TV Shows",
    "The Office": "TV Shows",
    "Hacks": "TV Shows",
    "Brooklyn 99": "TV Shows",
    "B99": "TV Shows",
    "Seinfeld": "TV Shows",
    "The Buccaneers": "TV Shows",
    "Severance": "TV Shows",
    "Parks and Recreation": "TV Shows",
    "*The Good Place*": "TV Shows",

    # Video Games
    "Clair Obscur": "Video Games",
    "Hades": "Video Games",
    "Rogue Legacy": "Video Games",
    "Rogue Legacy2": "Video Games",
    "Rogue": "Video Games",
    "Balatro": "Video Games",
    "Ring Fit Adventure": "Video Games",
    "Pentiment": "Video Games",
    "Diablo": "Video Games",
    "Diablo4": "Video Games",
    "Diablo 4": "Video Games",
    "Vampire Survivors": "Video Games",
    "Roller Coaster Tycoon 2": "Video Games",
    "Night in the Woods": "Video Games",
    "*Night in the Woods*": "Video Games",
    "Disco Elysium": "Video Games",
    "Civilization 3": "Video Games",
    "Tetris": "Video Games",
    "Rimworld": "Video Games",
    "*Elden Ring*": "Video Games",

    # Podcasts
    "Triple Click": "Podcasts",
    "99% Invisible": "Podcasts",
    "Get Played": "Podcasts",
    "Jordan Jesse Go!": "Podcasts",
    "Conan O'Brien Needs a Friend": "Podcasts",
}

# Duplicate groups: map variant names to a canonical name.
DUPLICATES = {
    "*The Secret History*": "The Secret History",
    "*The Lost Estate*": "The Lost Estate",
    "Baru": "The Traitor Baru Cormorant",
    "*Learning to Work*": "Learning to Work",
    "*Gentle Writing Advice*": "Gentle Writing Advice",
    "*War of Art*": "The War of Art",
    "*Silver Nitrate*": "Silver Nitrate",
    "*Buttercream*": "Buttercream",
    "*The Year's Best Software Writing*": "The Year's Best Software Writing",
    "*The Bear*": "The Bear",
    "B99": "Brooklyn 99",
    "Rogue Legacy2": "Rogue Legacy",
    "Rogue": "Rogue Legacy",
    "Diablo4": "Diablo",
    "Diablo 4": "Diablo",
    "*Night in the Woods*": "Night in the Woods",
    "*Elden Ring*": "Elden Ring",
    "*The Good Place*": "The Good Place",
}

CATEGORY_ORDER = ["Books", "TV Shows", "Video Games", "Podcasts"]
TOP_N = 5

# One color per category, cycling through the palette.
CATEGORY_COLORS = {cat: COLORS[i] for i, cat in enumerate(CATEGORY_ORDER)}


def main():
    setup_style()
    args = parse_viz_args(DEFAULT_INPUT)

    data = load_json(args.input)

    # Aggregate counts by canonical name and category
    category_items = defaultdict(lambda: defaultdict(int))

    for title, info in data.items():
        if title not in CATEGORIES:
            continue
        category = CATEGORIES[title]
        canonical = DUPLICATES.get(title, title)
        category_items[category][canonical] += info["count"]

    # Build per-category top lists
    sections = []
    for category in CATEGORY_ORDER:
        items = category_items.get(category, {})
        top = sorted(items.items(), key=lambda x: x[1], reverse=True)[:TOP_N]
        if top:
            sections.append((category, top))

    # Layout: one subplot per category, stacked vertically
    n_sections = len(sections)
    fig, axes = plt.subplots(
        n_sections, 1,
        figsize=(10, 2.2 * n_sections + 1.5),
        gridspec_kw={"hspace": 0.7},
    )
    if n_sections == 1:
        axes = [axes]

    fig.suptitle("Media consumed in 2025", fontsize=18, fontweight="bold", y=0.98)

    for ax, (category, top_items) in zip(axes, sections):
        names = [t[0] for t in reversed(top_items)]
        values = [t[1] for t in reversed(top_items)]
        color = CATEGORY_COLORS[category]

        bars = ax.barh(names, values, color=color, height=0.65)

        for bar in bars:
            width = bar.get_width()
            ax.text(
                width + 0.5, bar.get_y() + bar.get_height() / 2,
                str(int(width)),
                va="center", ha="left", fontsize=10, color=TEXT_COLOR,
            )

        ax.set_title(category, fontsize=14, fontweight="bold", loc="left")
        ax.set_xlim(0, max(values) * 1.18)
        ax.xaxis.set_visible(False)
        ax.grid(axis="y", visible=False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    save_figure(fig, "media_top")


if __name__ == "__main__":
    main()
