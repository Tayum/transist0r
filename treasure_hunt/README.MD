#### 1. Tested on Python 3.8.0
No additional libraries required.

#### 2. Run:
`$ python3 main.py`

You can change `main(use_example_map=True)` call to `main(use_example_map=False)` to get use of example map instead of inputting via `stdin`.

#### 3. Tests:
Run all tests:

`$ python3 -m unittest discover tests`

Run tests for input:

`$ python3 -m unittest discover -s tests -p 'test_input.py'`

Run tests for non-recursive solution:

`$ python3 -m unittest discover -s tests -p 'test_nonrecursive.py'`

Run tests for recursive solution:

`$ python3 -m unittest discover -s tests -p 'test_recursive.py'`
