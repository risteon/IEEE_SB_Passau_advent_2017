#!/usr/bin/env python3
from fractions import gcd
from operator import mul
from functools import reduce

__author__ = "Christoph Rist"
__license__ = "MIT"


def lcm(*numbers):
    """Lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


def main():
    """This algorithm is dimension-agnostic and can
       therefor be used for n-dimensional presents
    """
    dimensions = list(map(int, input().split()))
    edge_length = lcm(*dimensions)
    print(reduce(mul, [edge_length // x for x in dimensions]))


if __name__ == "__main__":
    main()

