#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        s = "0 = 0"
    else:
        s = " + ".join(map(str, L))
        s = s + " = " + str(sum(L))
    return s


def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation([]))


if __name__ == "__main__":
    main()

