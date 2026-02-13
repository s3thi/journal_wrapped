from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_media.md"


def process_entry(data, entry_filename, accumulator):
    if "media" in data and isinstance(data["media"], list):
        for item in data["media"]:
            accumulator[item].append(entry_filename)


def format_output(accumulator):
    return {
        item: {"count": len(entries), "entries": entries}
        for item, entries in accumulator.items()
    }


def main():
    run_extraction(
        task_name="media",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: defaultdict(list),
    )


if __name__ == "__main__":
    main()
