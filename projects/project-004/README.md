# Project 004 --- Array Indexing Challenge

**Phase:** 1 --- Python Foundations for MATLAB Programmers\
**Difficulty:** Beginner\
**Estimated time:** 2 hours\
**Main topics:** Python lists, indexing, slicing, negative indexing,
`len()`, and basic tests\
**Dataset:** Synthetic data created inside the program; no external
dataset is required.

## 1. Objective

Build a small Python program that extracts and rearranges values from a
list of measurements.

This project focuses on understanding how Python accesses sequences.
Since MATLAB uses **one-based indexing** and Python uses **zero-based
indexing**, pay particular attention to the position of each element.

You should implement the tasks yourself. Use the hints below if you get
stuck; the README intentionally does not provide the complete solution.

## 2. Scenario

Imagine you recorded these five temperature measurements:

``` python
temperatures = [21.5, 22.0, 21.8, 23.1, 22.7]
```

Your program should retrieve specific measurements, select ranges, and
create a reversed copy of the list.

## 3. Requirements and tasks

### Task 1 --- Inspect the list

1.  Create the `temperatures` list shown above.
2.  Print the entire list.
3.  Print the number of measurements using `len()`.
4.  Print the first and last measurements.

**Think about:** What index refers to the first element? How can you
access the last element without knowing the list's length?

### Task 2 --- Access individual elements

Print the following values:

-   The first measurement.
-   The third measurement.
-   The last measurement.
-   The second-to-last measurement.

Add a short comment explaining the difference between positive and
negative indexing.

### Task 3 --- Use slicing

Create and print these slices:

-   The first three measurements.
-   The measurements at positions 2 through 4, using ordinary human
    counting.
-   All measurements except the first and last.
-   The last three measurements.

Remember: in a slice `items[start:stop]`, `start` is included and `stop`
is excluded.

### Task 4 --- Reverse the list

Create a reversed version of the list and print it. Keep the original
list unchanged.

You may use slicing. Do not use a loop for this task unless you want an
extra challenge.

### Task 5 --- Write a reusable function

Write a function that accepts a list and returns its first and last
elements in a clearly defined format.

Consider how your function should behave when the list is empty. Choose
a sensible approach and document it.

### Task 6 --- Test your program

Check your code with at least these cases:

1.  The original five-element list.
2.  A list containing one element.
3.  An empty list.
4.  A list containing negative and positive numbers.
5.  A list containing strings.

For each test, record what you expected and what actually happened. Make
sure your function handles an empty list intentionally rather than
accidentally raising an unhandled error.

## 4. Expected output

Your output can be formatted differently, but it should communicate the
requested values clearly. For the original list, the results should
include:

``` text
Measurements: [21.5, 22.0, 21.8, 23.1, 22.7]
Number of measurements: 5
First measurement: 21.5
Third measurement: 21.8
Last measurement: 22.7
Second-to-last measurement: 23.1
First three: [21.5, 22.0, 21.8]
Last three: [21.8, 23.1, 22.7]
```

Your program should also print the other required slices and the
reversed list.

## 5. MATLAB-to-Python comparison

  Concept              MATLAB            Python
  -------------------- ----------------- ---------------------
  First element        `A(1)`            `items[0]`
  Third element        `A(3)`            `items[2]`
  Last element         `A(end)`          `items[-1]`
  Number of elements   `numel(A)`        `len(items)`
  Select a range       `A(2:4)`          `items[1:4]`
  Reverse a sequence   Often `flip(A)`   Often `items[::-1]`

The range expressions differ because MATLAB indexing begins at 1 and
includes the end index, while Python indexing begins at 0 and excludes
the slice's stop index.

## 6. Suggested project structure

``` text
python-data-analyst/
└── projects/
    └── project-004/
        ├── main.py
        └── README.md
```

Keep the code in `main.py` and this specification in `README.md`.

## 7. How to run

Open a terminal in the `project-004` folder and run:

``` bash
python main.py
```

If your system uses the Python launcher on Windows, this may also work:

``` powershell
py main.py
```

## 8. Success criteria

-   [ ] The program runs without syntax errors.
-   [ ] You can access elements using positive and negative indices.
-   [ ] You correctly use slices, including the exclusive stop index.
-   [ ] You create a reversed copy without changing the original list.
-   [ ] Your reusable function has a clear behavior for an empty list.
-   [ ] You manually test the required cases and compare actual versus
    expected results.
-   [ ] Your variable names and output labels are understandable.
-   [ ] You can explain why Python's `items[1:4]` selects the second,
    third, and fourth elements.

## 9. Hints (not the complete solution)

-   Python's first list index is `0`.
-   Use `len(items)` to get the number of elements.
-   Negative indices count backward from the end: `-1` refers to the
    last element.
-   The stop index in a slice is excluded.
-   `items[::-1]` is a common way to create a reversed copy.
-   Before accessing `items[0]` or `items[-1]`, consider what happens if
    the list is empty.
-   For tests, print the input, expected result, and actual result, or
    use simple `assert` statements once you understand them.

## 10. Extension challenge

Create a function that accepts a list and a number `n`, then returns the
first `n` elements. Decide what should happen when `n` is negative or
larger than the list length. Test your decisions with at least three
cases.

## 11. Reflection

After finishing, answer these questions in your own words:

1.  Why does Python use zero-based indexing in many sequences?
2.  What does the exclusive stop index make easier when calculating
    slice lengths?
3.  What is the difference between `items[-1]` and
    `items[len(items) - 1]`?
4.  Why should an empty list be tested?
5.  Which indexing difference from MATLAB was easiest to forget?

## 12. Portfolio potential

This is primarily a **practice project**, not a flagship portfolio item.
Keep it in your learning repository because it establishes foundational
Python fluency. The key achievement is being able to reason about
indices and test edge cases without relying on a tutorial.
