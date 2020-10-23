#!/usr/bin/env python3
def triple(x):
	return 3* x


def square(x):
	return x**2


def main():
    for i in range(1, 11):
    	t = triple(i)
    	s = square(i)

    	if t < s:
    		break
    	print(f"triple({i})=={t} square({i})=={s}")

if __name__ == "__main__":
    main()
