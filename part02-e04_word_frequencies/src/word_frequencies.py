#!/usr/bin/env python3

def word_frequencies(filename):
    d = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.rstrip().split()
            words = [x.strip("""!"#$%&'()*,-./:;?@[]_""") for x in words]
            if not words:
                continue
            for word in words:
                if word in d.keys():
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
    return d


def main():
    d = word_frequencies("alice.txt")
    for k, v in d.items():
        print(f"{k}\t{v}")


if __name__ == "__main__":
    main()

