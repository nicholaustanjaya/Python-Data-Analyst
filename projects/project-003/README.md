# Project 003: Statistical Summary Calculator

**Phase:** Python Foundations\
**Difficulty:** Beginner\
**Estimated time:** 2 hours\
**Primary skills:** Lists, loops, built-in functions, numeric
calculations, basic input validation\
**Dataset:** Synthetic measurement values created in the program or
entered by the user

## 1. Objective

Build a Python program that summarizes a collection of numerical
measurements. The program should report the number of values, minimum,
maximum, and arithmetic mean.

This project introduces a common data-analysis workflow: take a
collection of observations and calculate a few descriptive statistics.
You will use synthetic data, so no external dataset or additional
package is required.

## 2. Problem statement

Imagine you collected several measurements from an experiment. Instead
of calculating each summary manually, write a script named
`statistics_summary.py` that calculates and displays a concise report.

Start with a small, hard-coded list of numbers. Once the basic version
works, consider allowing the user to enter measurements.

## 3. Requirements

Your program should:

1.  Store several numeric measurements in a Python list.
2.  Calculate how many measurements are present.
3.  Find the minimum and maximum values.
4.  Calculate the arithmetic mean.
5.  Display the results with clear labels.
6.  Handle the empty-list case intentionally so the program does not
    attempt to calculate a mean when there are no values.

### Constraints

-   Use only the Python standard library.
-   Do not use NumPy or pandas for this project.
-   Use meaningful variable names.
-   Avoid repeating the same calculation logic unnecessarily.
-   Do not worry about median or standard deviation yet; those can be
    added as extensions.

## 4. Suggested milestones

### Milestone 1 --- Create the data

Create a list of at least five numeric values. Use plausible measurement
values, such as temperatures or sensor readings.

### Milestone 2 --- Calculate the summary

Use Python's built-in functions where appropriate:

-   `len()` to count values
-   `min()` to find the smallest value
-   `max()` to find the largest value
-   `sum()` to calculate the total, which you can use to calculate the
    mean

The arithmetic mean is:

\[ `\text{mean}`{=tex} =
`\frac{\text{sum of values}}{\text{number of values}}`{=tex} \]

Remember that the number of values must not be zero when calculating the
mean.

### Milestone 3 --- Make the output readable

Print a short report with labels and sensible numeric formatting. The
exact wording is up to you.

Example format (illustrative only):

``` text
STATISTICAL SUMMARY
-------------------
Number of measurements: 5
Minimum:                2.50
Maximum:               10.00
Mean:                   6.10
```

Your numbers will depend on your chosen data.

### Milestone 4 --- Check your result

Verify your program with a small dataset whose answer you can calculate
by hand. Also check what happens when the list is empty.

## 5. How to run

From the project directory, run:

``` bash
python statistics_summary.py
```

If your system uses the Python launcher on Windows, this may also work:

``` powershell
py statistics_summary.py
```

## 6. Success criteria

The project is complete when:

-   [ ] The script runs without syntax errors.
-   [ ] It correctly counts the measurements.
-   [ ] The minimum and maximum match the chosen data.
-   [ ] The mean is correct.
-   [ ] The output is clearly labeled and readable.
-   [ ] The empty-list case is handled without an unhandled
    division-by-zero error.
-   [ ] You can explain how each result is calculated.
-   [ ] You have tested at least one dataset manually.

## 7. MATLAB-to-Python connection

In MATLAB, you might summarize a vector using functions such as `numel`,
`min`, `max`, and `mean`.

Python has related built-ins for basic lists:

``` python
values = [2.5, 4.0, 6.0, 8.0, 10.0]

count = len(values)
minimum = min(values)
maximum = max(values)
average = sum(values) / len(values)
```

This snippet illustrates the relevant operations; adapt them into your
own program rather than copying a complete solution. Python list
indexing starts at zero, and a list is not automatically a vectorized
numerical array as it is in a typical MATLAB workflow.

## 8. Extension challenges

Choose one after the required version works:

1.  Ask the user to enter values separated by commas.
2.  Reject invalid numeric input with a helpful error message.
3.  Add the median without importing a library.
4.  Put the summary calculations inside a function that accepts a list
    and returns a result.
5.  Write the summary to a text file.

## 9. Reflection

When you finish, write a few sentences answering:

-   Why does the mean change when an unusually large value is added?
-   Why must the empty-list case be handled separately?
-   Which parts would be different if you used a NumPy array instead of
    a Python list?

## 10. Deliverables

Your project folder should contain:

``` text
project-003/
├── statistics_summary.py
└── README.md
```

Keep the README updated if you add extension features. When publishing
the project, include a short example run and explain any assumptions you
made.
