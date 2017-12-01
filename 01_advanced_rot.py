#!/usr/bin/env python3
import sys
import string

__author__ = "Christoph Rist"
__license__ = "MIT"

"""
As there are 26 characters in the input alphabet, 3ROT13 equals ROT13.
"""

DEBUG = False

rot13 = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "nopqrstuvwxyzabcdefghijklm") 

def main():

    if DEBUG:
        sys.stdin = open("samples/01.1_input.txt")

    n = int(input())
    sizes = []
    for _ in range(n):
        print(str.translate(input(), rot13))


if __name__ == "__main__":
    main()

