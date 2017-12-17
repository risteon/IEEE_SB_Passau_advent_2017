#!/usr/bin/env python3
import sys
import collections
from operator import itemgetter
from queue import PriorityQueue

__author__ = "Christoph Rist"
__license__ = "MIT"


class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    @classmethod
    def as_leaf(cls, value):
        return cls(None, None, value)

    def leafs(self):
        return self.left, self.right

    def __lt__(self, other):
        if not self.value:
            return self.left < other
        elif not other.value:
            return self < other.left
        else:
            return self.value < other.value


def create_huffman_coding(freqs):
    q = PriorityQueue()
    for value in freqs:
        q.put((value[1], Node.as_leaf(value[0])))

    while q.qsize() > 1:
        l, r = q.get(), q.get()
        node = Node(l[1], r[1])
        q.put((l[0] + r[0], node))

    return q.get()


def walk_tree(node, prefix="", code={}):

    if node.left.value is None:
        walk_tree(node.left, prefix + "0", code)
    else:
        code[node.left.value] = prefix + "0"
    if node.right.value is None:
        walk_tree(node.right, prefix + "1", code)
    else:
        code[node.right.value] = prefix + "1"
    return code


def main():
    """
    """
    if True:
        sys.stdin = open("samples/07.1_input.txt")

    chars = list(sys.stdin.read().strip())
    freq = collections.Counter(chars)
    root = create_huffman_coding(freq.most_common())

    code = walk_tree(root[1])
    s = sorted(code.items(), key=itemgetter(0), reverse=False)
    for char, encoding, in s:
        print("{} {}".format(char, encoding))


if __name__ == "__main__":
    main()

