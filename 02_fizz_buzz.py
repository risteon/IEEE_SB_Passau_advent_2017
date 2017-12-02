#!/usr/bin/env python3
import sys

__author__ = "Christoph Rist"
__license__ = "MIT"

"""
"""

def main():
    n, k = map(int, input().split())

    reactions = []
    for _ in range(n):
        a, b = input().split()
        reactions.append((int(a), b))

    # discard empty line
    input()
    # for each number to test
    for _ in range(k):
        t = int(input())
        matches = [reaction for divisor, reaction in reactions
                                if t % divisor == 0]
        # print output
        if not matches:
            print(t)
        else:
            print(*matches, sep=' ')


if __name__ == "__main__":
    main()

