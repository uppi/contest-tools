#!/usr/bin/env python3

import sys
import glob
import os
import subprocess
import re
import time
import traceback
import filecmp

IN_FILE_ID = re.compile("input(.+)\.txt$")


def main(executable, test_dir):
    last_noncustom = None
    for input_file in sorted(glob.glob(os.path.join(test_dir, "input*.txt"))):
        if "custom" in input_file:
            if last_noncustom is not None:
                if filecmp.cmp(input_file, last_noncustom):
                    continue
        else:
            last_noncustom = input_file
        print(input_file)
        with open(input_file) as input_fobj:
            try:
                start_time = time.time()
                output = subprocess.check_output(
                    [executable], stdin=input_fobj, shell=True)
                elapsed_time = time.time() - start_time
                print("Time spent: {:.2f} seconds".format(elapsed_time))
                output = output.decode().strip()
                test_id = IN_FILE_ID.findall(input_file)[0]
                output_file = os.path.join(
                    test_dir, "ans{}.txt".format(test_id))
                with open(output_file) as ans_f:
                    needed_output = ans_f.read().strip()
                    if needed_output != output:
                        print("Mismatch at test {}".format(test_id))
                        print("Needed: {}\n=====\nReal: {}".format(
                            needed_output, output))
                    else:
                        print("Test {} passed".format(test_id))
            except Exception:
                traceback.print_exc()


if __name__ == '__main__':
    main(*sys.argv[1:])
