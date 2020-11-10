#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n == 1:
        return np.eye(1, dtype=int)
    else:
        a = np.eye(n, dtype=int)
        b = np.concatenate((np.flip(a, axis=1), a))
        e = np.concatenate((b, np.flip(b, axis=1)), axis=1)
        e = np.delete(e, n, axis=0)
        e = np.delete(e, n, axis=1)
    return e

def main():
    pass

if __name__ == "__main__":
    main()

