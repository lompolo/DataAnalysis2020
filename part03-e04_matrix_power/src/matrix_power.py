#!/usr/bin/env python3
import numpy as np
from numpy.linalg import inv
from functools import reduce


def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0])
    
    if n < 0:
        n *= -1
        a = inv(a)
    
    A = (a for _ in range(n))
    return reduce(np.matmul, A)
    

def main():
    return

if __name__ == "__main__":
    main()

