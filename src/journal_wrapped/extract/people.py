from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_people.md"


def process_entry(data, entry_filename, accumulator):
    if "people" in data and isinstance(data["people"], list):
        for person in data["people"]:
            accumulator[person].append(entry_filename)


def format_output(accumulator):
    return {
        person: {"count": len(entries), "entries": entries}
        for person, entries in accumulator.items()
    }


def main():
    run_extraction(
        task_name="people",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: defaultdict(list),
    )


if __name__ == "__main__":
    main()