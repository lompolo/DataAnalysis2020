#!/usr/bin/env python3

def extract_numbers(s):
    numbers = []

    for i in s.split():
        try:
            numbers.append(int(i))
        except ValueError as identifier:
            try:
                numbers.append(float(i))
            except ValueError as identifier:
                pass

    return numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()

