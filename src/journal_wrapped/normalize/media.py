from journal_wrapped.lib.common import PROMPTS_DIR
from journal_wrapped.lib.normalizer import run_normalization

PROMPT_PATH = PROMPTS_DIR / "normalize_media.md"


def main():
    run_normalization(
        task_name="media",
        prompt_path=PROMPT_PATH,
        output_map_key="media_map",
    )


if __name__ == "__main__":
    main()
