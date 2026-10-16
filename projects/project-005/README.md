# Project 5: Matrix Operations with Lists

**Roadmap phase:** Python Foundations\
**Difficulty:** Beginner\
**Estimated time:** 2--3 hours\
**Primary file:** `matrix_operations.py`\
**Libraries:** Python standard library only --- do not use NumPy or
pandas in this project\
**Data:** Small, synthetic matrices defined in your code

------------------------------------------------------------------------

## 1. Project Overview

In this project, you will represent matrices using **nested Python
lists** and write functions that perform basic matrix operations.

For example, this matrix:

``` python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

has 2 rows and 3 columns. Each inner list represents one row.

You already have some experience with MATLAB arrays and matrices. This
project helps you understand how matrix-like data is represented and
processed in core Python before introducing NumPy later in the roadmap.

### Why this project matters

Matrices are common in engineering and data analysis. Working with
nested lists gives you practice with loops, indexing, function design,
input validation, and algorithmic thinking. In later projects, NumPy
will make numerical operations more concise and efficient.

------------------------------------------------------------------------

## 2. Learning Objectives

By the end of this project, you should be able to:

-   Represent a matrix using a list of lists.
-   Read matrix dimensions using `len()`.
-   Access an element using row and column indices.
-   Traverse a matrix with nested `for` loops.
-   Add two matrices with matching dimensions.
-   Multiply two compatible matrices using the matrix-multiplication
    rule.
-   Validate matrix dimensions before calculating.
-   Write reusable functions and test them with small examples.
-   Explain one important difference between MATLAB matrices and nested
    Python lists.

------------------------------------------------------------------------

## 3. Requirements and Constraints

Use only concepts and tools you have learned so far.

-   Python 3.13 or another compatible Python 3 version.
-   Python standard library only.
-   No NumPy, pandas, or other third-party libraries.
-   Use nested lists to store matrices.
-   Put each operation in a clearly named function.
-   Include basic validation and helpful error messages.
-   Keep the code readable with meaningful variable names and comments
    where useful.

**Important:** Implement the functions yourself. This README describes
the requirements and provides hints, but it intentionally does not
include the complete solution.

------------------------------------------------------------------------

## 4. Project Structure

Create the following folder and files in your existing roadmap
repository:

``` text
python-data-analyst/
└── projects/
    └── project-005/
        ├── README.md
        └── matrix_operations.py
```

If your repository uses a slightly different naming convention, keep it
consistent with your earlier projects.

------------------------------------------------------------------------

## 5. Tasks and Milestones

### Task 1 --- Define sample matrices

In `matrix_operations.py`, define at least three small matrices as
nested lists:

1.  A 2 × 2 matrix.
2.  Another 2 × 2 matrix.
3.  A 2 × 3 matrix.

Use small integers so you can verify the calculations by hand.

Example matrix definition:

``` python
matrix_a = [
    [1, 2],
    [3, 4],
]
```

Do not copy this example as your only test case; create additional
matrices yourself.

### Task 2 --- Inspect matrix dimensions

Create a function that reports the number of rows and columns in a
matrix.

Requirements:

-   Return the row count.
-   Return the column count.
-   Handle an empty matrix deliberately.
-   Check that all rows have the same number of columns, or document how
    your function responds to an irregular matrix.

Test your function with a square matrix, a rectangular matrix, and an
empty matrix.

### Task 3 --- Access and display matrix elements

Create a function that prints a matrix in a readable row-by-row format.

Requirements:

-   Print each row on its own line.
-   Display the values in their original order.
-   Do not assume that every matrix is square.

Also demonstrate accessing a specific element using row and column
indices. Remember that Python indexing starts at `0`.

### Task 4 --- Add two matrices

Create a function that adds two matrices element by element.

Requirements:

-   The matrices must have the same number of rows and columns.
-   If their dimensions differ, report the problem clearly.
-   Return a **new matrix** rather than modifying either input matrix.
-   Test the function with both positive and negative values.

Mathematical rule:

\[ C\_{ij} = A\_{ij} + B\_{ij} \]

Here, (A) and (B) are the input matrices and (C) is the result.

### Task 5 --- Multiply two matrices

Create a function for **matrix multiplication**, not element-by-element
multiplication.

If matrix (A) has dimensions (m `\times `{=tex}n), and matrix (B) has
dimensions (n `\times `{=tex}p), the product (C = AB) has dimensions (m
`\times `{=tex}p).

Requirements:

-   The number of columns in the first matrix must equal the number of
    rows in the second matrix.
-   Calculate each output element using a row from the first matrix and
    a column from the second matrix.
-   Return a new matrix.
-   Reject incompatible dimensions with a clear message.
-   Test at least one non-square multiplication, such as a 2 × 3 matrix
    multiplied by a 3 × 2 matrix.

The calculation for one output element follows this rule:

\[ C\_{ij} = `\sum`{=tex}*{k=0}\^{n-1} A*{ik}B\_{kj} \]

You can implement the summation with loops; you do not need a special
library.

### Task 6 --- Demonstrate and organize the results

In the main part of the script:

1.  Print the sample input matrices.
2.  Print their dimensions.
3.  Display the result of matrix addition.
4.  Display the result of matrix multiplication.
5.  Show what happens when you attempt an invalid operation.

Use labels so a reader can distinguish each matrix and result.

------------------------------------------------------------------------

## 6. MATLAB vs. Python: Key Differences

  -----------------------------------------------------------------------
  Topic                   MATLAB                  Python lists
  ----------------------- ----------------------- -----------------------
  Indexing                Starts at `1`           Starts at `0`

  Matrix representation   Built-in numeric matrix Nested lists for this
                          type                    project

  Matrix dimensions       Commonly `size(A)`      Commonly `len(A)` for
                                                  rows and `len(A[0])`
                                                  for columns, after
                                                  validation

  Matrix multiplication   `A * B` for standard    Must implement the
                          numeric matrices        matrix-multiplication
                                                  algorithm yourself in
                                                  this project

  Element-wise            `A .* B`                Must implement
  multiplication                                  separately with lists;
                                                  do not confuse it with
                                                  matrix multiplication
  -----------------------------------------------------------------------

**Keep in mind:** A nested Python list is not the same thing as a MATLAB
numeric matrix. Python lists can also contain inconsistent row lengths
or mixed data types, so your code should validate the structure before
performing matrix calculations.

Later, in the NumPy phase, you will learn how `numpy.ndarray` supports
concise array and matrix calculations.

------------------------------------------------------------------------

## 7. Suggested Manual Test Cases

Use these cases to check your implementation. Work out the expected
results by hand before running your code.

### Test A --- Matrix addition

``` text
A = [[1, 2],
     [3, 4]]

B = [[10, 20],
     [30, 40]]
```

Expected result:

``` text
[[11, 22],
 [33, 44]]
```

### Test B --- Matrix multiplication

``` text
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]
```

Expected result:

``` text
[[58, 64],
 [139, 154]]
```

### Test C --- Incompatible dimensions for addition

Try adding a 2 × 2 matrix and a 2 × 3 matrix. Your program should not
silently calculate an incorrect result.

### Test D --- Incompatible dimensions for multiplication

Try multiplying a 2 × 3 matrix by a 2 × 2 matrix. The inner dimensions
do not match, so your function should report an error.

### Test E --- Empty or irregular matrix

Test an empty list and a nested list with rows of different lengths,
such as `[[1, 2], [3]]`. Your code should handle these cases
deliberately rather than failing unexpectedly.

------------------------------------------------------------------------

## 8. Expected Output Format

Your exact output may differ, but it should be clear and labeled. For
example:

``` text
MATRIX OPERATIONS
=================

Matrix A:
1 2
3 4

Matrix B:
10 20
30 40

A + B:
11 22
33 44

A x B:
...
```

Include the dimensions and a readable error message when an operation is
invalid. The multiplication result depends on the matrices you choose.

------------------------------------------------------------------------

## 9. Completion Checklist

-   [ ] I represented matrices as nested lists.
-   [ ] I wrote a function to inspect matrix dimensions.
-   [ ] I handled empty and irregular matrices deliberately.
-   [ ] I wrote a function to display matrices clearly.
-   [ ] I implemented matrix addition using loops.
-   [ ] I implemented matrix multiplication using loops.
-   [ ] I validated dimensions before each operation.
-   [ ] I returned new matrices instead of modifying the inputs.
-   [ ] I tested valid and invalid operations.
-   [ ] I compared nested Python lists with MATLAB matrices.
-   [ ] I added comments where they clarify the algorithm.
-   [ ] I committed the finished project to Git.

------------------------------------------------------------------------

## 10. Hints (Without the Full Solution)

-   Use `len(matrix)` to get the number of rows.
-   For a non-empty, rectangular matrix, `len(matrix[0])` gives the
    number of columns.
-   Use one loop for rows and another for columns when visiting each
    element.
-   For matrix multiplication, think in terms of **row × column**, not
    matching positions.
-   A result matrix can be built by creating rows and appending
    calculated values.
-   Check dimensions before entering the calculation loops.
-   Decide how your functions will signal invalid input: for example,
    raise `ValueError` with a helpful message, or follow a consistent
    error-handling style you have already used.
-   Keep each function responsible for one task.

If you get stuck, first write the algorithm in plain English or
pseudocode, then translate one step at a time into Python.

------------------------------------------------------------------------

## 11. Extension Challenge (Optional)

Once the required operations work:

1.  Add matrix subtraction.
2.  Add element-wise multiplication as a separate function, with a name
    that distinguishes it from matrix multiplication.
3.  Add a function that transposes a matrix (rows become columns).
4.  Create a small test function that checks known inputs against
    expected outputs.
5.  Compare your list-based implementation with NumPy after you finish
    this project. Keep NumPy code in a separate experiment so the core
    implementation remains dependency-free.

------------------------------------------------------------------------

## 12. Reflection Questions

Answer these in your own words in your notes or at the end of this
README:

1.  Why does matrix multiplication require the first matrix's column
    count to match the second matrix's row count?
2.  Why is matrix multiplication different from element-wise
    multiplication?
3.  What problems can arise if rows in a nested list have different
    lengths?
4.  How does Python's zero-based indexing differ from MATLAB's indexing?
5.  What part of the implementation would become simpler with NumPy, and
    what does writing it manually teach you?

------------------------------------------------------------------------

## 13. Portfolio Notes

This is an early learning project, so it does not need to be a flagship
portfolio piece. Its value is showing your understanding of loops,
nested data structures, reusable functions, and validation.

Before publishing it:

-   Ensure the script runs from a clean environment.
-   Remove debugging output and unused variables.
-   Keep the README aligned with what your code actually does.
-   Include a short explanation of your approach and any limitations.
-   Do not claim features you have not implemented.

**Next step:** Implement `matrix_operations.py` independently. Run the
manual test cases, then share your code and output for review. You can
ask for a hint or code review before requesting a complete solution.
