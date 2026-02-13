from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_social.md"


def process_entry(data, entry_filename, accumulator):
    if "social_activities" in data and isinstance(data["social_activities"], list):
        for activity in data["social_activities"]:
            accumulator[activity].append(entry_filename)


def format_output(accumulator):
    return {
        activity: {"count": len(entries), "entries": entries}
        for activity, entries in accumulator.items()
    }


def main():
    run_extraction(
        task_name="social",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: defaultdict(list),
    )


if __name__ == "__main__":
    main()