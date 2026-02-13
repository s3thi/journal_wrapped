"""Social events summary -- markdown output."""

from collections import defaultdict
from pathlib import Path

from journal_wrapped.viz.social_data import RECURRING_GROUPS, ONE_OFF_EVENTS
from journal_wrapped.viz.style import load_json, parse_viz_args, OUTPUT_DIR

DEFAULT_INPUT = "out/llama/social_*.json"


def main():
    args = parse_viz_args(DEFAULT_INPUT)
    data = load_json(args.input)

    # Aggregate recurring communities
    community_counts = defaultdict(int)
    for event_name, info in data.items():
        if event_name in RECURRING_GROUPS:
            canonical = RECURRING_GROUPS[event_name]
            community_counts[canonical] += info["count"]

    # Sort by count descending
    sorted_communities = sorted(
        community_counts.items(), key=lambda x: x[1], reverse=True
    )

    # Collect one-off events that exist in the data
    one_offs = []
    for event_name in ONE_OFF_EVENTS:
        if event_name in data:
            one_offs.append(event_name)

    # Build markdown
    lines = ["# Social life in 2025", ""]

    lines.append("## Recurring communities")
    lines.append("")
    for name, count in sorted_communities:
        lines.append(f"- **{name}**: {count} sessions")
    lines.append("")

    lines.append("## Notable events")
    lines.append("")
    for event in one_offs:
        lines.append(f"- {event}")
    lines.append("")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "social_summary.md"
    output_path.write_text("\n".join(lines))
    print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
