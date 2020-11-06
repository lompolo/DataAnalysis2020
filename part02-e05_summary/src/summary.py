#!/usr/bin/env python3

import sys
from statistics import stdev, mean


def summary(filename):
    with open(filename, "r") as f:
        numbers = []
        for n in f.readlines():
            try:
                numbers.append(float(n.strip("\n")))
            except ValueError:
                """skip"""
    return sum(numbers), mean(numbers), stdev(numbers)


def main():
    names = sys.argv[1:]
    for i in names:
        s, m, std = summary(i)
        print(f"File: {i} Sum: {s:.6f} Average: {m:.6f} Stddev: {std:.6f}")


if __name__ == "__main__":
    main()

