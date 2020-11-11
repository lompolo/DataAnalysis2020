#!/usr/bin/env python3

import numpy as np
from scipy.linalg import norm


def vector_angles(X, Y):
    return np.degrees(np.arccos(np.clip(np.sum(X * Y, axis=1) / (norm(X, axis=1) * norm(Y, axis=1)), -1, 1)))

def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    b = np.random.randint(0, 10, (4, 4))
    vector_angles(a, b)

if __name__ == "__main__":
    main()

