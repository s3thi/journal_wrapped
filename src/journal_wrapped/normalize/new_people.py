from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.normalizer import run_normalization

PROMPT_PATH = PROMPTS_DIR / "normalize_new_people.md"


def main():
    run_normalization(
        task_name="new_people",
        prompt_path=PROMPT_PATH,
        output_map_key="new_people_map",
    )


if __name__ == "__main__":
    main()
