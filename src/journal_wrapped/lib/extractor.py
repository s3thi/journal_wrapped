import os

from journal_wrapped.lib.common import (
    JOURNAL_ENTRIES_PATH,
    OUTPUT_DIR,
    create_output_path,
    discover_journal_entries,
    get_largest_entries,
    load_model,
    load_prompts,
    parse_args,
    process_journal_entry,
    save_results,
)


def run_extraction(
    task_name, prompt_path, process_entry, format_output, create_accumulator
):
    """
    Generic runner for extraction tasks.

    Args:
        task_name (str): Name of the task (used for output filename).
        prompt_path (str): Path to the markdown prompt file.
        process_entry (callable): Function(data, entry_filename, accumulator) to update accumulator.
        format_output (callable): Function(accumulator) -> output_data dict.
        create_accumulator (callable): Factory function() -> initial accumulator structure.
    """
    args = parse_args()

    system_prompt = load_prompts(prompt_path)
    accumulator = create_accumulator()

    model, tokenizer = load_model(args.model)

    all_entries = discover_journal_entries(JOURNAL_ENTRIES_PATH)
    if not all_entries:
        return

    is_partial = False
    if args.limit:
        is_partial = True
        total_found = len(all_entries)
        all_entries = get_largest_entries(all_entries, JOURNAL_ENTRIES_PATH, args.limit)
        print(
            f"Found {total_found} entries, processing largest {len(all_entries)} using model {args.model}."
        )
    else:
        print(f"Found {len(all_entries)} entries to process using model {args.model}.")

    total_entries = len(all_entries)

    for i, (month, entry_filename) in enumerate(all_entries, 1):
        print(f"[{i}/{total_entries}] Processing {month}/{entry_filename}...")
        month_path = os.path.join(JOURNAL_ENTRIES_PATH, month)

        try:
            with open(os.path.join(month_path, entry_filename)) as f:
                journal_text = f.read()

            data = process_journal_entry(model, tokenizer, system_prompt, journal_text)
            if data is None:
                print(f"Warning: failed to extract JSON from {entry_filename}, skipping.")
                continue
            process_entry(data, entry_filename, accumulator)

        except Exception as e:
            print(f"Error processing {entry_filename}: {e}")

    output_data = format_output(accumulator)
    output_path = create_output_path(
        OUTPUT_DIR, task_name, args.model, partial=is_partial
    )
    save_results(output_data, output_path)
