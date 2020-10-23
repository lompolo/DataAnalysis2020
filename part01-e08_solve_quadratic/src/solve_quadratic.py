#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    q = math.sqrt(b**2 - 4*a*c)
    x1 = (-b - q) / (2*a)
    x2 = (-b + q) / (2*a)
    return round(x2, 6), round(x1, 6)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    print(solve_quadratic(2.633689, 8.690866, 5.326800))
    print(solve_quadratic(-2.0, 2.0, 1.0))


if __name__ == "__main__":
    main()
