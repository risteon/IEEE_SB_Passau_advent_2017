#!/usr/bin/env python3
import operator
import itertools
import sys

__author__ = "Christoph Rist"
__license__ = "MIT"


def generate_perm_lists(target_sums):
    yield[2, 2, 2, 2]


def find_min_costs(diffs):

    if not diffs:
        raise RuntimeError("wrong diffs:empty")
    for d in diffs:
        if d >= 0:
            raise RuntimeError("wrong diffs")

    to_reach = [len(diffs), len(diffs) + 1]

    min_cost = 0

    for l in generate_perm_lists(to_reach):
        for perm in itertools.permutations(l):
            index = -2
            c = 0
            for p in perm:
                index += p
                c += diffs[index]
            if c < min_cost:
                min_cost = c

    return min_cost


def main():
    """
    """
    if True:
        sys.stdin = open("samples/05.1_input.txt")

    n = int(input())
    costs_green = []
    costs_red = []
    for _ in range(n):
        g, r = map(int, input().split())
        costs_green.append(g)
        costs_red.append(r)
    diffs = [a - b for a, b, in zip(costs_green, costs_red)]

    begin = 0
    total = 0
    for index, diff in enumerate(diffs):
        if diff >= 0:
            if index > begin:
                total += find_min_costs(diffs[begin:index])
                total += sum(costs_red[begin:index])

            total += costs_red[index]
            begin = index + 1

    if begin != len(diffs):
        total += find_min_costs(diffs[begin:])
        total += sum(costs_red[begin:])

    print(total)


if __name__ == "__main__":
    main()
