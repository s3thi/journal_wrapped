"""CLI entry point for Journal Wrapped.

Usage:
    jw <stage> <task> [task-specific args ...]

Stages: extract, normalize, viz
"""

import importlib
import pkgutil
import sys


STAGES = ("extract", "normalize", "viz")


def _available_tasks(stage):
    pkg = importlib.import_module(f"journal_wrapped.{stage}")
    return sorted(
        name
        for _importer, name, _ispkg in pkgutil.iter_modules(pkg.__path__)
        if name != "__init__"
    )


def _print_help():
    print("usage: jw <stage> <task> [args ...]\n")
    print("stages:")
    for stage in STAGES:
        tasks = _available_tasks(stage)
        print(f"  {stage:12s} {', '.join(tasks)}")
    print()


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        _print_help()
        sys.exit(0)

    stage = args[0]
    if stage not in STAGES:
        print(f"error: unknown stage '{stage}'\n")
        _print_help()
        sys.exit(1)

    if len(args) < 2 or args[1] in ("-h", "--help"):
        tasks = _available_tasks(stage)
        print(f"usage: jw {stage} <task> [args ...]\n")
        print(f"available tasks: {', '.join(tasks)}")
        sys.exit(0)

    task = args[1]
    module_name = f"journal_wrapped.{stage}.{task}"

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        tasks = _available_tasks(stage)
        print(f"error: unknown task '{task}' in stage '{stage}'\n")
        print(f"available tasks: {', '.join(tasks)}")
        sys.exit(1)

    # Strip stage and task from argv so argparse in the module sees only its own flags.
    sys.argv = [f"jw {stage} {task}"] + args[2:]
    module.main()


if __name__ == "__main__":
    main()
