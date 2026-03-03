"""Main module for ng-wc."""

import argparse
import os
from pathlib import Path


def main(*args, **kwargs) -> None:
    """Count words in a file.

    Parses and displays the word count from a specified file using argparse.
    Supports optional count filtering for specific word patterns.

    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(prog="NG Word Count", description="Parses word count in files")
    parser.add_argument("-c", "--count", action="store_true")
    parser.add_argument("file_path")

    args = parser.parse_args()

    file_path = Path(args.file_path)

    print(f"{os.path.getsize(file_path)} {file_path.name}")


if __name__ == "__main__":  # pragma: no cover
    main()
