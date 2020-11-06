#!/usr/bin/env python3

def reverse_dictionary(d):
    r = {}

    for k, v in d.items():
        for i in v:
            if i in r:
                r[i].append(k)
            else:
                r[i] = [k]

    return r


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()

