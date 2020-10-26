# Enter you module contents here

"""
This module provides functions to calculate:
hypothenuse(): calculate length of hypothenuse of triangle
area(): calculate of triangle
"""

__version__ = '1.0'
__author__ = 'Tero Lompolo'

import math


def hypothenuse(a, b):
    """Calculate length of hypothenuse of triangle"""
    return math.sqrt(a**2 + b**2)


def area(a, b):
    """Calculate are of triangle"""
    return 0.5 * a * b

