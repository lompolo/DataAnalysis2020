#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    formatted = []

    pattern = re.compile(r"^\s*(\d{1,3})\s+(\d{1,3})+\s+(\d{1,3})+\s+(.+)$")
    with open(filename, "r") as f:
        for i in f:
            x = pattern.search(i)
            if not x:
                continue
            elif len(x.groups()) < 4:
                continue
            formatted.append(f"{x.group(1)}\t{x.group(2)}\t{x.group(3)}\t{x.group(4)}")

    return formatted


def main():
    print(red_green_blue(filename="rgb.txt"))


if __name__ == "__main__":
    main()

