#!/usr/bin/env python3
import sys
import os


def parse_codeforces(text):
    """
    Примеры
    входные данные
    3
    R 0 1
    B 1 0
    R 1 1
    выходные данные
    4
    входные данные
    3
    R 3 0
    R 2 0
    R 1 0
    выходные данные
    6
    """
    tests = [t.split("выходные данные") for t in text.split("входные данные")
             if "выходные данные" in t]
    tests = [(i.strip(), o.strip()) for i, o in tests]
    return tests


def save_tests(dir_name, tests):
    directory = os.path.join("tests", dir_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i, t in enumerate(tests):
        inp, ans = t
        with open(os.path.join(
                directory, "input{}.txt".format(i + 1)), "w") as out:
            out.write(inp)
            out.write("\n")
        with open(os.path.join(
                directory, "ans{}.txt".format(i + 1)), "w") as out:
            out.write(ans)
            out.write("\n")
    inp, ans = tests[-1] if tests else ("", "")
    for i in range(8):
        with open(os.path.join(
                directory, "input_custom{}.txt".format(i + 1)), "w") as out:
            out.write(inp)
            out.write("\n")
        with open(os.path.join(
                directory, "ans_custom{}.txt".format(i + 1)), "w") as out:
            out.write(ans)
            out.write("\n")


if __name__ == '__main__':
    problem_name = input("Type problem name: ").strip()
    print("Paste tests:")
    text = sys.stdin.read().strip()
    tests = parse_codeforces(text)
    save_tests(problem_name, tests)
