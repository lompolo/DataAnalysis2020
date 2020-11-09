#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rows = []
    r, c = a.shape
    for i in range(r):
        rows.append(np.array(a[i, :]))
    return rows


def get_columns(a):
    cols = []
    t = a.T
    r, c = t.shape
    for i in range(r):
        cols.append(t[i, :])
    return cols


def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()

