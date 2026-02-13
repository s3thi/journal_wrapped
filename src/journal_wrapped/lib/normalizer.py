import argparse
import json
import os
from collections import defaultdict

from journal_wrapped.lib.common import (
    call_llm,
    extract_json,
    load_model,
    save_results,
)


def load_normalization_prompt(prompt_path):
    with open(prompt_path, "r") as f:
        return f.read()


def get_normalization_mapping(model, tokenizer, prompt_template, terms):
    if not terms:
        return {}

    terms_json = json.dumps(terms)
    user_message = (
        f"Here is the list of terms to normalize:\n```json\n{terms_json}\n```"
    )

    print(f"Requesting normalization for {len(terms)} terms...")
    response = call_llm(model, tokenizer, prompt_template, user_message)
    mapping = extract_json(response)

    if not isinstance(mapping, dict):
        print("Warning: LLM did not return a valid dictionary. Returning empty mapping.")
        return {}

    return mapping


def apply_mapping(original_map, mapping):
    new_map = defaultdict(list)
    # original_map is {issue_name: [list of files]} OR {issue_name: {'entries': [list of files], ...}}
    # mapping is {issue_name: canonical_name}

    for issue, value in original_map.items():
        canonical = mapping.get(issue, issue)  # Fallback to original if missing
        
        files = []
        if isinstance(value, list):
            files = value
        elif isinstance(value, dict) and "entries" in value:
            files = value["entries"]
        
        new_map[canonical].extend(files)

    # Deduplicate file lists
    for issue in new_map:
        new_map[issue] = sorted(list(set(new_map[issue])))

    return dict(sorted(new_map.items()))


def run_normalization(
    task_name, prompt_path, output_map_key, input_key=None, output_sick_days_key=None
):
    parser = argparse.ArgumentParser(
        description=f"Normalize {task_name} data extracted from journals."
    )
    parser.add_argument(
        "input_file",
        type=str,
        help=f"Path to the input JSON file (output of {task_name}.py)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="mlx-community/Qwen3-32B-4bit",
        help="Model to use for normalization",
    )
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        return

    print(f"Loading data from {args.input_file}...")
    with open(args.input_file, "r") as f:
        data = json.load(f)

    # Determine the map to normalize
    if input_key:
        if input_key not in data:
            print(
                f"Error: Input key '{input_key}' not found in data. "
                f"Available keys: {list(data.keys())}"
            )
            return
        input_map = data[input_key]
    else:
        # Assume the root object is the map if no key is provided
        input_map = data

    if not isinstance(input_map, dict):
        print(f"Error: Input data (at key '{input_key}') is not a dictionary.")
        return

    model, tokenizer = load_model(args.model)
    system_prompt = load_normalization_prompt(prompt_path)

    # Normalize
    terms = list(input_map.keys())
    print(f"\n--- Normalizing {task_name.replace('_', ' ').title()} Terms ---")
    mapping = get_normalization_mapping(model, tokenizer, system_prompt, terms)
    new_map = apply_mapping(input_map, mapping)

    output_data = {
        output_map_key: new_map,
        "normalization_mapping": mapping,
    }

    if output_sick_days_key:
        new_sick_days = set()
        for files in new_map.values():
            new_sick_days.update(files)
        output_data[output_sick_days_key] = sorted(list(new_sick_days))

    # Determine output path
    dirname, basename = os.path.split(args.input_file)
    name_part, ext = os.path.splitext(basename)
    output_filename = f"{name_part}_normalized{ext}"
    output_path = os.path.join(dirname, output_filename)

    save_results(output_data, output_path)