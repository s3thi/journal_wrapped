from collections import defaultdict
from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.extractor import run_extraction

TASK_PROMPT_PATH = PROMPTS_DIR / "extract_physical_health.md"


def process_entry(data, entry_filename, accumulator):
    physical_sick_days, physical_sickness_map = accumulator

    if "physical_health_issues" in data and isinstance(
        data["physical_health_issues"], list
    ):
        issues = data["physical_health_issues"]
        if issues:
            physical_sick_days.add(entry_filename)
            for issue in issues:
                physical_sickness_map[issue].append(entry_filename)


def format_output(accumulator):
    physical_sick_days, physical_sickness_map = accumulator
    return {
        "physical_sick_days": sorted(list(physical_sick_days)),
        "physical_sickness_map": dict(sorted(physical_sickness_map.items())),
    }


def main():
    run_extraction(
        task_name="physical_health",
        prompt_path=TASK_PROMPT_PATH,
        process_entry=process_entry,
        format_output=format_output,
        create_accumulator=lambda: (set(), defaultdict(list)),
    )


if __name__ == "__main__":
    main()