# Tools for programming contests

Test automation using python3 and Sublime Text

## Generate tests
Run `tools/gentests.py` and insert your **problem_name**, then copy-paste sample tests as is. Only codeforces format is supported so far:

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

## Clear unused tests

After you finish your work, you may want to clear the custom tests you didn't change. To reveal them, run `tools/show_unused_tests.py`. You may want to run `tools/show_unused_tests.py | xargs rm` to remove them.

