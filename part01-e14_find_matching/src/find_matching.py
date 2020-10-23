#!/usr/bin/env python3

def find_matching(L, pattern):
    r = []

    if not L or not pattern:
        return r

    for i, w in enumerate(L):
        if pattern in w:
            r.append(i)
    return r


def main():
    print(find_matching(["jack", "paul"], ""))
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()

