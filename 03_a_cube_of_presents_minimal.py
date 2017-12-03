#!/usr/bin/env python3
from fractions import gcd
from operator import mul
from functools import reduce

d = list(map(int, input().split()))
print(reduce(mul, map(lambda x: reduce(lambda a, b: (a*b)//gcd(a, b), d)//x, d)))

