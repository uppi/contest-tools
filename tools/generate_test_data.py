#!/usr/bin/env python3
import sys
import random
import functools

HELP_MSG = """
Usage: tools/generate_test_data.py FROM_IDX END_IDX 'CALLBACK'

Examples:

> tools/generate_test_data.py 2 20 '\"{} {}\".format(i, \" \".join(list(map(str, range(3, i * 2)))))'
2 3
3 3 4 5
4 3 4 5 6 7
5 3 4 5 6 7 8 9
...

> tools/generate_test_data.py 0 200 '"{} {}".format(i, " ".join(map(str, random.sample(rng(200000), 10))))'
0 165071 69526 51919 146370 22430 179599 183854 171458 38744 62598
1 84871 61983 82583 196561 72424 161388 36854 109100 153300 199365
...

"""


@functools.lru_cache(maxsize=1000)
def rng(*args):
    return list(range(*args))


def main(callback_str):
    callback_str = "lambda i: " + callback_str
    callback = eval(callback_str)
    for i in range(start, end):
        print(callback(i))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(HELP_MSG)
    else:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        callback_str = sys.argv[3]
        main(callback_str)
