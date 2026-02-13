from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_mental_health.md"


def process_entry(data, entry_filename, accumulator):
    mental_sick_days, mental_health_map = accumulator

    if "mental_health_issues" in data and isinstance(
        data["mental_health_issues"], list
    ):
        issues = data["mental_health_issues"]
        if issues:
            mental_sick_days.add(entry_filename)
            for issue in issues:
                mental_health_map[issue].append(entry_filename)


def format_output(accumulator):
    mental_sick_days, mental_health_map = accumulator
    return {
        "mental_sick_days": sorted(list(mental_sick_days)),
        "mental_health_map": dict(sorted(mental_health_map.items())),
    }


def main():
    run_extraction(
        task_name="mental_health",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: (set(), defaultdict(list)),
    )


if __name__ == "__main__":
    main()