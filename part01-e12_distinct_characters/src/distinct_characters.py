#!/usr/bin/env python3

def distinct_characters(L):
    s = dict()

    for p in L:
        s[p] = len(set(p))

    return s


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()

