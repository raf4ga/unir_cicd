"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING_ORDER = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Couldn't sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ASCENDING_ORDER
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        if (len(sys.argv) == 4 and sys.argv[3] in ['asc', 'desc']):
            ascending_order = sys.argv[3] == 'asc'
    else:
        print("You must specify the file path as the first argument")
        print("You must indicate in second argument if you want to delete duplicated lines (yes/no)")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} doesn't exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending_order))
