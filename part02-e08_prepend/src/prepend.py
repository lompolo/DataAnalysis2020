#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param):
        self.prepend = param

    def write(self, param):
        print(f"{self.prepend}{param}")

def main():
    pass

if __name__ == "__main__":
    main()

