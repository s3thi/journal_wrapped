from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.normalizer import run_normalization

PROMPT_PATH = PROMPTS_DIR / "normalize_mental_health.md"


def main():
    run_normalization(
        task_name="mental_health",
        prompt_path=PROMPT_PATH,
        output_map_key="mental_health_map",
        input_key="mental_health_map",
        output_sick_days_key="mental_sick_days",
    )


if __name__ == "__main__":
    main()
