from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.normalizer import run_normalization

PROMPT_PATH = PROMPTS_DIR / "normalize_physical_health.md"


def main():
    run_normalization(
        task_name="physical_health",
        prompt_path=PROMPT_PATH,
        output_map_key="physical_sickness_map",
        input_key="physical_sickness_map",
        output_sick_days_key="physical_sick_days",
    )


if __name__ == "__main__":
    main()
