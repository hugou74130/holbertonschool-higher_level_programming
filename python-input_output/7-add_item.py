#!/usr/bin/python3
"""
This module contains the function `add_item` that adds all command-line
arguments to a Python list and then saves them to a file.
"""
import sys
import os
import importlib.util


def _load_module(path, name):
    """Dynamically load a module from the given file path and return it."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CUR_DIR = os.path.dirname(os.path.abspath(__file__))

# Load helper modules (they live in the same directory)
save_mod = _load_module(
    os.path.join(CUR_DIR, '5-save_to_json_file.py'),
    'save_to_json_file_mod'
)
load_mod = _load_module(
    os.path.join(CUR_DIR, '6-load_from_json_file.py'),
    'load_from_json_file_mod'
)

save_to_json_file = save_mod.save_to_json_file
load_from_json_file = load_mod.load_from_json_file


if __name__ == '__main__':
    filename = os.path.join(CUR_DIR, 'add_item.json')
    args = sys.argv[1:]

    try:
        data = load_from_json_file(filename)
    except Exception:
        data = []

    data.extend(args)
    save_to_json_file(data, filename)
