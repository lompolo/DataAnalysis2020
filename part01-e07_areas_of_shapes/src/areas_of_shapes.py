import math


def triangle(b, h):
    return 0.5 * b * h


def circle(r):
    return math.pi * r ** 2


def rectangle(w, h):
    return w * h


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")

        if shape == "":
            break
        elif shape == 'triangle':
            b = int(input("Give base of the triangle: "))
            h = int(input("Give height of the triangle: "))
            print(f"The area is {triangle(b, h):.6f}")
        elif shape == 'rectangle':
            w = int(input("Give width of the rectangle: "))
            h = int(input("Give height of the rectangle: "))
            print(f"The area is {rectangle(w, h):.6f}")
        elif shape == 'circle':
            r = int(input("Give radius of the circle: "))
            print(f"The area is {circle(r):.6f}")
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
