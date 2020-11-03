#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    listing = []
    try:
        with open(filename, "r") as file:
            for i in file:
                x = re.search(r"(\d{2,}) (\w{3})\s+(\d{1,2}) (\d{2}):(\d{2}) ([-a-zA-Z0-9_.]+)$", i).groups()
                listing.append(tuple(map(lambda k: int(k) if k.isdigit() else k, list(x))))

    except FileNotFoundError:
        print("File not found")

    return listing


def main():
    f = file_listing(filename="listing.txt")
    print(f)


if __name__ == "__main__":
    main()

