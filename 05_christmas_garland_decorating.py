#!/usr/bin/env python3

__author__ = "Christoph Rist"
__license__ = "MIT"


def find_min_costs(costs, diffs):
    if not costs:
        return 0

    for index, diff in enumerate(diffs):
        if diff > 0:
            return costs[index][1]\
                + find_min_costs(costs[:index], diffs[:index])\
                + find_min_costs(costs[index+1:], diffs[index+1:])

    costs_green, costs_red = zip(*costs)
    return min(sum(costs_green[::2]) + sum(costs_red[1::2]),
            sum(costs_red[::2]) + sum(costs_green[1::2]))


def main():
    """
    """
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(tuple(map(int, input().split())))
    diffs = list(map(lambda x: x[0] - x[1], costs))
    print(find_min_costs(costs, diffs))


if __name__ == "__main__":
    main()

