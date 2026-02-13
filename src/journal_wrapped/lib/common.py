import argparse
import json
import os
import re
from pathlib import Path

from mlx_lm import generate, load

# Configuration constants
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
PROMPTS_DIR = PROJECT_ROOT / "prompts"
JOURNAL_ENTRIES_PATH = "/path/to/entries"
CORE_PROMPT_PATH = PROMPTS_DIR / "core.md"
OUTPUT_DIR = PROJECT_ROOT / "out"
MAX_TOKENS = 32768


def extract_json(response):
    """
    Extracts a JSON string from a response that may contain a fenced code block
    and parses it into a Python dictionary.
    """
    match = re.search(r"```(json)?\s*(.*?)\s*```", response, re.DOTALL)
    if match:
        json_string = match.group(2).strip()
    else:
        json_string = response.strip()

    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        print(f"Failed to decode JSON: {json_string}")
        return None


def load_prompts(task_prompt_path):
    """
    Load and concatenate core and task-specific prompts.
    """
    with open(CORE_PROMPT_PATH) as f:
        core_prompt = f.read()

    with open(task_prompt_path) as f:
        task_prompt = f.read()

    return core_prompt + "\n" + task_prompt


def load_model(model_name):
    """
    Load and return the model and tokenizer using mlx_lm.
    """
    print(f"Loading model {model_name}...")
    model, tokenizer = load(path_or_hf_repo=model_name)
    print("Model loaded successfully.")
    return model, tokenizer


def discover_journal_entries(base_path):
    """
    Scan directories and return a list of (month, filename) tuples.
    """
    all_entries = []

    if not os.path.isdir(base_path):
        print(f"Error: Journal path {base_path} not found.")
        return all_entries

    months = [m for m in os.listdir(base_path) if not m.startswith(".")]

    for month in months:
        month_path = os.path.join(base_path, month)
        if os.path.isdir(month_path):
            journal_entries = [
                j for j in os.listdir(month_path) if not j.startswith(".")
            ]
            for j in journal_entries:
                all_entries.append((month, j))

    all_entries.sort()
    return all_entries


def get_largest_entries(all_entries, base_path, limit):
    """
    Sort entries by file size (largest first) and return the top N.
    """
    entries_with_size = []

    for month, filename in all_entries:
        file_path = os.path.join(base_path, month, filename)
        try:
            file_size = os.path.getsize(file_path)
            entries_with_size.append(((month, filename), file_size))
        except OSError:
            continue

    entries_with_size.sort(key=lambda x: x[1], reverse=True)

    return [entry for entry, size in entries_with_size[:limit]]


def create_output_path(output_dir, prefix, model_name, partial=False):
    """
    Generate a safe output file path.
    """
    safe_model_name = model_name.replace("/", "-")
    if partial:
        output_filename = f"{prefix}_partial_{safe_model_name}.json"
    else:
        output_filename = f"{prefix}_{safe_model_name}.json"
    return os.path.join(output_dir, output_filename)


def save_results(data, output_path):
    """
    Handle directory creation and JSON writing.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Extraction complete. Data written to {output_path}")


def call_llm(model, tokenizer, system_prompt, user_message):
    """
    Send a system + user message to the LLM and return the raw response text.
    """
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    prompt = tokenizer.apply_chat_template(
        conversation=conversation, add_generation_prompt=True
    )

    return generate(
        model=model,
        tokenizer=tokenizer,
        prompt=prompt,
        max_tokens=MAX_TOKENS,
        verbose=False,
    )


def process_journal_entry(model, tokenizer, system_prompt, journal_text):
    """
    Generate LLM response using mlx_lm and extract JSON from it.
    Returns None if JSON extraction fails.
    """
    user_message = f"<journal_entry>\n{journal_text}\n</journal_entry>"
    response = call_llm(model, tokenizer, system_prompt, user_message)
    return extract_json(response)


def parse_args():
    """
    Create and configure argument parser for journal processing scripts.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--limit", type=int, help="Process only the N largest entries by file size"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="mlx-community/Qwen3-32B-4bit",
        help="Model to use for analysis",
    )
    return parser.parse_args()
