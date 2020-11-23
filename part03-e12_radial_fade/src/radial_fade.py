#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    h, w = a.shape[:2]
    return (h - 1) / 2, (w - 1) / 2   # note the order: (center_y, center_x)


def radial_distance(a):
    h, w = a.shape[:2]
    y, x = center(a)

    yx_list = list([j - y, i - x] for j in range(h) for i in range(w))
    return np.linalg.norm(yx_list, axis=1).reshape(h, w)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    b = radial_distance(a.copy())
    return np.interp(b, (b.min(), b.max()), (0, 1))


def radial_mask(a):
    return np.subtract(1, scale(a))


def radial_fade(a):
    return a.copy() * radial_mask(a)[:, :, np.newaxis]


def main():
    image = plt.imread("painting.png")
    _, ax = plt.subplots(3, 1)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()

