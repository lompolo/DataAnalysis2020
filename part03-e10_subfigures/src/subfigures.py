#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x = a[:, 0]
    y = a[:, 1]
    color = a[:, 2]
    size = a[:, -1]
    
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y)
    ax[1].scatter(x, y, c=color, s=size)
    plt.show()

def main():
    a = np.array([1,2,3,4,5,6,7,8,2,2,2,2,10,20,30,40]).reshape(4,4)
    subfigures(a)

if __name__ == "__main__":
    main()
