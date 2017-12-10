#!/usr/bin/env python3
import operator

__author__ = "Christoph Rist"
__license__ = "MIT"


def find_min_costs(costs, diffs):

    costs_green, costs_red = zip(*costs)
    smallest = min(sum(costs_green[::2]) + sum(costs_red[1::2]),
            sum(costs_red[::2]) + sum(costs_green[1::2]))

    max_index, _ = max(enumerate(diffs), key=operator.itemgetter(1))

    cost = costs_green[max_index]
    if max_index > 0:
        cost += costs_red[max_index-1]
    if max_index < len(costs) - 1:
        cost += costs_red[max_index+1]

    if max_index > 1:
        cost += find_min_costs(costs[:max_index-1], diffs[:max_index-1])
    if max_index < len(costs) - 2:
        cost += find_min_costs(costs[max_index+2:], diffs[max_index+2:])

    return min(smallest, cost)


def main():
    """
    """
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(tuple(map(int, input().split())))
    diffs = list(map(lambda x: x[1] - x[0], costs))

    begin = 0
    total = 0
    for index, diff in enumerate(diffs):
        if diff <= 0:
            if index > begin:
                total += find_min_costs(costs[begin:index], diffs[begin:index])
            total += costs[index][1]
            begin = index + 1

    if begin != len(diffs):
        total += find_min_costs(costs[begin:], diffs[begin:])

    print(total)


if __name__ == "__main__":
    main()
