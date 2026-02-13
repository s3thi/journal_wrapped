from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_travel.md"


def process_entry(data, entry_filename, accumulator):
    if "travel" in data and isinstance(data["travel"], list):
        for trip in data["travel"]:
            accumulator[trip].append(entry_filename)


def format_output(accumulator):
    return {
        trip: {"count": len(entries), "entries": entries}
        for trip, entries in accumulator.items()
    }


def main():
    run_extraction(
        task_name="travel",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: defaultdict(list),
    )


if __name__ == "__main__":
    main()