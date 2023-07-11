"""
Files-related functions
"""
import os
import sys
import datetime
from pathlib import Path

def create_directory_list(args):
    def build_output(entry, long=False):
        if long:
            size = entry.stat().st_size
            date = datetime.datetime.fromtimestamp(
                entry.stat().st_mtime).strftime(
                "%b %d %H:%M:%S"
            )
            return f"{size:>6d} {date} {entry.name}"
        return entry.name

    target_dir = Path(args.path)

    # Check if target directory exists
    if not target_dir.exists():
        # Does not exists
        print("The target directory doesn't exist")
        raise SystemExit(1)

    # Iterate through all values returned from the path search
    for entry in target_dir.iterdir():
        # Print out output
        print(build_output(entry, long=True))

