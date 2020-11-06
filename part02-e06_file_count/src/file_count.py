#!/usr/bin/env python3

import sys


def file_count(filename):
    no_of_lines, no_of_words, no_of_chars = 0, 0, 0
    with open(filename, "r") as file:
        for line in file:
            no_of_lines += 1
            no_of_chars += len(line)

            words = line.split()
            no_of_words += len(words)

    return no_of_lines, no_of_words, no_of_chars


def main():
    files = sys.argv[1:]
    for f in files:
        l, w, c = file_count(f)
        print(f"{l}\t{w}\t{c}\t{f}")


if __name__ == "__main__":
    main()

