#!/usr/bin/env python3

from itertools import groupby


def detect_ranges(L):
    sorted_list = sorted(L)
    new_list = []

    for i, j in groupby(enumerate(sorted_list), lambda l: l[1] - l[0]):
        k = list(j)
        if len(k) > 1:
            new_list.append((k[0][1], k[-1][1]+1))
        else:
            new_list.append(k[0][1])
    return new_list


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()

