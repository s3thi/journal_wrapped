from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.normalizer import run_normalization

PROMPT_PATH = PROMPTS_DIR / "normalize_social.md"


def main():
    run_normalization(
        task_name="social",
        prompt_path=PROMPT_PATH,
        output_map_key="social_map",
    )


if __name__ == "__main__":
    main()
