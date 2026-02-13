# AGENTS.md for journal_wrapped

This is a project to analyze my personal journal entries from the year 2025 and extract data from them using a local LLM. The idea is to use the extracted data to create a summary of my year in the style of Spotify Wrapped.

## LLM framework

All code runs on an M4 MacBook Pro with 48GB RAM. Models are loaded using Apple's `mlx_lm` library.

## uv

The project is managed using `uv`. Scripts are run via the `jw` CLI:

```bash
uv run jw <stage> <task> [args ...]
```

For example:

```bash
uv run jw extract gratitude --limit 5
uv run jw normalize people out/llama/people_model.json
uv run jw viz people
```

Don't try to use the `python` executable directly. Never run any scripts as part of your development workflow. The user will run them and paste the output, if required.

## Python style

Never use type annotations in your output. We don't need them for this project.

## Prompts

System prompts are stored in the `prompts/` directory. Most system prompts will have two parts: a core prompt that lives in `prompts/core.md`, and a task-specific prompt. The full system prompt is formed by concatenating the two.

## Source

Source code lives in `src/journal_wrapped/`, organized into subpackages:

- `lib/` — shared utilities (LLM loading, extraction runner, normalization runner)
- `extract/` — extraction scripts (one per data type)
- `normalize/` — normalization scripts (one per data type)
- `viz/` — visualization scripts
