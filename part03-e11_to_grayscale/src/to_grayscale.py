#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    weights = [.2126, .7152, .0722]
    return np.dot(image[:, :, :3], weights)


def to_red(image):
    image[:, :, 1:] = 0
    return image

def to_green(image):
    image[:, :, [0, 2]] = 0
    return image

def to_blue(image):
    image[:, :, :-1] = 0
    return image

def main():
    img = plt.imread("src/painting.png")
    plt.gray()
    plt.imshow(to_grayscale(img))
    _, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(img.copy()))
    ax[1].imshow(to_green(img.copy()))
    ax[2].imshow(to_blue(img.copy()))
    plt.show()

if __name__ == "__main__":
    main()

