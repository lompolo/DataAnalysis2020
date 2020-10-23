#!/usr/bin/env python3

def merge(L1, L2):
    """This fucntion merges to lists together and performs bubble sort in ascending order"""
    new_list = L1 + L2
    last = len(new_list) - 1

    for i in range(last, 0, -1):
        for j in range(i):
            if new_list[j] > new_list[j+1]:
                t = new_list[j]
                new_list[j] = new_list[j+1]
                new_list[j+1] = t

    return new_list


def main():
    L1 = [1, 2, 4, 3, 5]
    L2 = [3, 2, 9, 5, 7]
    L3 = [10, 15, 11, 13]

    print(merge(L1, L2))
    print(merge(L2, L3))


if __name__ == "__main__":
    main()

