"""Shared style and helpers for all Journal Wrapped visualizations."""

import argparse
import glob
import json
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

from journal_wrapped.lib.common import OUTPUT_DIR as _BASE_OUTPUT_DIR


# --- Color palette (muted, warm tones) ---

COLORS = [
    "#c0583d",  # warm terracotta
    "#d4915e",  # muted orange
    "#e8c170",  # warm gold
    "#7a9b76",  # sage green
    "#5b8a8a",  # teal
    "#6b7b8d",  # slate blue
    "#9b7e9b",  # muted purple
    "#c48a8a",  # dusty rose
    "#a0856e",  # warm brown
    "#8faaaa",  # light teal
]

BAR_COLOR = COLORS[0]
BAR_COLOR_ALT = COLORS[4]

BACKGROUND = "#faf7f2"
TEXT_COLOR = "#3a3a3a"
GRID_COLOR = "#e0dbd3"


# --- Style setup ---

def setup_style():
    """Apply the shared matplotlib style."""
    plt.rcParams.update({
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,
        "axes.edgecolor": GRID_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "axes.grid": True,
        "grid.color": GRID_COLOR,
        "grid.alpha": 0.5,
        "grid.linewidth": 0.5,
        "text.color": TEXT_COLOR,
        "xtick.color": TEXT_COLOR,
        "ytick.color": TEXT_COLOR,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "axes.titlepad": 16,
        "font.family": "sans-serif",
        "font.size": 11,
        "figure.dpi": 100,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.3,
        "savefig.facecolor": BACKGROUND,
    })


# --- Output helpers ---

OUTPUT_DIR = _BASE_OUTPUT_DIR / "viz"


def save_figure(fig, name):
    """Save figure as both SVG and PNG to out/viz/."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_DIR / f"{name}.svg", format="svg")
    fig.savefig(OUTPUT_DIR / f"{name}.png", format="png")
    print(f"Saved {OUTPUT_DIR / name}.svg and .png")
    plt.close(fig)


# --- Date parsing ---

def parse_date(filename):
    """Parse a date from a journal filename like '2025-01-15.md'."""
    return datetime.strptime(filename.replace(".md", ""), "%Y-%m-%d")


# --- Data loading ---

def parse_viz_args(default_input):
    """Parse common viz arguments. Each viz script provides its own default glob pattern."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", default=default_input,
        help="Glob pattern or path to input JSON file",
    )
    return parser.parse_args()


def load_json(pattern):
    """Load a single JSON file matching the given glob pattern."""
    matches = sorted(glob.glob(str(pattern)))
    if not matches:
        raise FileNotFoundError(f"No file found matching {pattern}")
    path = matches[0]
    with open(path) as f:
        return json.load(f)
