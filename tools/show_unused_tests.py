#!/usr/bin/env python3

import os
import glob
import filecmp
import re

INPUT_ARG = re.compile("input([a-z1-9_]+).txt")


def show_unused_customs(test_dir):
    last_noncustom = None
    for input_file in sorted(glob.glob(os.path.join(test_dir, "input*.txt"))):
        if "custom" in input_file:
            if last_noncustom is not None:
                if filecmp.cmp(input_file, last_noncustom):
                    arg = INPUT_ARG.findall(input_file)[0]
                    print(input_file)
                    print(os.path.join(
                        test_dir, "ans{}.txt".format(arg)))
        else:
            last_noncustom = input_file


if __name__ == '__main__':
    for testdir in os.listdir("tests"):
        show_unused_customs(
            os.path.join(os.path.abspath("tests"), testdir))
