# Tools for programming contests

Test automation using python3 and Sublime Text

## Add sample and boilerplate tests
Run `tools/parse_and_generate_tests.py` and insert your **problem_name**, then copy-paste sample tests as is. Only codeforces format is supported so far:

```
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
```

Press `Ctrl+D` after you paste everything you wanted. If you don't have any sample tests and still want to create empty custom tests, just press `Ctrl+D`.

The tests will be added as `tests/$problem_name/(input|ans)[1-n].txt`. Also, the last test will be copied as a couple of `tests/$problem_name/(input|ans)_custom[1-n].txt` tests. It is done to make custom test creation easier.

## Run tests

To run the tests, use `tools/run_tests.py ./a.out tests/$problem_name` or `tools/run_tests.py ./a.py tests/$problem_name`. You should `chmod +x` your python sources.

To be able to run tests from Sublime Text with `Ctrl+B`, you should name your solution source file with the same **problem_name** basename: e. g. `a.cpp` for `tests/a/...`. Only python and C++ (assuming you have g++ in the PATH) are supported in the `contest.sublime-project`.

## Generate complex tests

To generate complex tests for performance testing, use `tools/generate_test_data.py`. It is a helper script which iterates through a given range of iterations and generates test output according to the given callback. 

Usage: `tools/generate_test_data.py FROM_IDX END_IDX 'CALLBACK'`

### Examples

`$ tools/generate_test_data.py 2 20 '"{} {}".format(i, " ".join(list(map(str, range(3, i * 2)))))'`

    2 3
    3 3 4 5
    4 3 4 5 6 7
    5 3 4 5 6 7 8 9
    ...

`$ tools/generate_test_data.py 0 200 '"{} {}".format(i, " ".join(map(str, random.sample(rng(200000), 10))))'`

    0 165071 69526 51919 146370 22430 179599 183854 171458 38744 62598
    1 84871 61983 82583 196561 72424 161388 36854 109100 153300 199365
    ...

Full test generation:

    echo 200000 > tests/d/input_custom8.txt
    ../../tools/generate_test_data.py 0 200000 '"{} {}".format(random.randint(0, 100000), i)' >> tests/d/input_custom8.txt
    echo 2000 >> tests/d/input_custom8.txt
    ../../tools/generate_test_data.py 0 2000 '"{} {}".format(100, " ".join(map(str, random.sample(rng(100000), 100))))' >> tests/d/input_custom8.txt

## Clear unused tests

After you finish your work, you may want to clear the custom tests you didn't change. To reveal them, run `tools/show_unused_tests.py`. You may want to run `tools/show_unused_tests.py | xargs rm` to remove them.

