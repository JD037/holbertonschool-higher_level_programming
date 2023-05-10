#!/usr/bin/python3
import sys


def main():
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(total)


if __name__ == "__main__":
    main()
