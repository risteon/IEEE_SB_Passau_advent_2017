#!/usr/bin/env python3
import sys

__author__ = "Christoph Rist"
__license__ = "MIT"


def read_matrx():
    chars = []
    width = None
    while True:
        line = input()
        if not line:
            break
        chars.extend(line)
        if not width:
            width = len(line)
        elif width != len(line):
            raise RuntimeError("invalid input")

    return chars, width


def read_words():
    words = [line for line in sys.stdin]
    return list(map(lambda s: s.strip(), words))


def get_pos_string(word, matrix, width):

    def get_at(index):
        if index < 0 or index >= len(matrix):
            return None
        return matrix[index]

    def index_to_str(index):
        h = index//width
        w = index % width
        return chr(65 + h) + chr(65 + w)

    def check(index):
        if matrix[index] != word[0]:
            return None

        dirs = {'N': -width, 'O': 1, 'S': width, 'W': -1}
        for direction, diff in dirs.items():
            current_index = index + diff
            for c in word[1:]:
                actual = get_at(current_index)
                if not actual or actual != c:
                    break
                current_index += diff
            else:
                return index_to_str(index) + direction

        return None

    for i in range(len(matrix)):
        a = check(i)
        if a is not None:
            return a

    raise RuntimeError('Not found')


def main():
    """
    """
    m = read_matrx()
    words = read_words()
    print(''.join(map(lambda w: get_pos_string(w, *m), words)))


if __name__ == "__main__":
    main()

