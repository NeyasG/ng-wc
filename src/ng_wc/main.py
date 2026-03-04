"""Main module for ng-wc."""

import argparse
import os
from pathlib import Path


def main(argv: list[str] | None = None) -> None:
    """Count words in a file.

    Parses and displays the word count from a specified file using argparse.
    Supports optional count filtering for specific word patterns.

    Args:
        argv: Optional list of arguments

    Returns:
        None
    """
    parser = argparse.ArgumentParser(prog="NG Word Count", description="Parses word count in files")
    parser.add_argument("-c", "--count", help="Count the number of bytes in a file.", action="store_true")
    parser.add_argument("-l", "--lines", help="Outputs the number of lines in a file", action="store_true")
    parser.add_argument("file_path", nargs="?", help="Path to input file")

    args = parser.parse_args(argv)

    if args.file_path is None and not (args.count or args.lines):
        parser.print_help()
        return

    if args.file_path is None:
        parser.error("the following arguments are required: file_path")

    if not args.count and not args.lines:
        parser.print_help()
        return

    file_path = Path(args.file_path)

    if not file_path.is_file():
        print(f"The file {file_path!s} is not a valid file, or does not exist.")
        raise SystemExit(1)

    if args.count:
        print(f"{os.path.getsize(file_path)} {file_path.name}")

    if args.lines:
        with open(file_path) as f:
            print(f"{sum(1 for _ in f)} {file_path.name}")


if __name__ == "__main__":  # pragma: no cover
    main()
