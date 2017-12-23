#!/usr/bin/env python3
__author__ = "Christoph Rist"
__license__ = "MIT"


def main():
    n = int(input())
    for _ in range(n):
        trees = sorted(map(int, input().split()), reverse=True)
        print(max(map(lambda  x: x[0] + x[1], enumerate(trees))))


if __name__ == "__main__":
    main()

