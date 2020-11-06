#!/usr/bin/env python3

def file_extensions(filename):
    list_ex = []
    dic_ex = {}
    f = filename[1]
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip("\n")
                pair = line.split(".")
                if len(pair) < 2:
                    list_ex.append(pair[0])
                else:
                    if pair[-1] not in dic_ex.keys():
                        files = [line]
                    else:
                        files = dic_ex.get(pair[-1])
                        files.append(line)
                    dic_ex[pair[-1]] = files
    except:
        pass
    return list_ex, dic_ex


def main():
    l, d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    for key in sorted(d.keys()):
        print(f"{key} {len(d[key])}")

if __name__ == "__main__":
    main()

