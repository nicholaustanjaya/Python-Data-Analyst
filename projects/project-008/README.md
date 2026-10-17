# Project 8: Reusable Calculation Library

## Project Overview

- **Project Number:** 008
- **Difficulty:** Beginner
- **Estimated Time:** 2–3 hours
- **Phase:** Phase 1 — Python Foundations for MATLAB Programmers
- **Main Topics:** Functions, parameters, return values, docstrings, modules, imports
- **Primary Libraries:** Python standard library
- **Dataset:** No external dataset required

## 1. Objective

Build a reusable Python calculation library containing functions for common numerical and statistical operations.

Instead of defining every calculation directly inside one main script, you will separate the calculation functions into a Python module and import them into another script.

This project introduces an important principle in software development:

**Write a function once, then reuse it wherever it is needed.**

You will also learn how to document functions so that other developers can understand their purpose, inputs, outputs, and limitations.

## 2. Background

In previous projects, you implemented numerical calculations, statistical summaries, and engineering measurement simulations.

As programs become more complicated, placing every calculation in a single Python file makes the code harder to maintain and reuse.

For example, imagine that you need to calculate the mean of measurement data in several different programs. Instead of copying the same calculation repeatedly, you can define a function in a separate module and import it whenever necessary.

Python modules provide a straightforward way to organize this functionality.

## 3. Learning Objectives

By completing this project, you should be able to:

1. Define functions with parameters and return values.
2. Understand the difference between returning a result and printing it.
3. Write descriptive function names and docstrings.
4. Organize related functions into a Python module.
5. Import and call functions from another Python file.
6. Reuse functions without duplicating code.
7. Handle invalid inputs appropriately.
8. Test functions using multiple inputs.
9. Explain how Python modules compare with MATLAB function files.

## 4. Project Requirements

Create a small library for numerical calculations.

Your library should include functions for:

- Calculating the mean of a sequence of numbers.
- Finding the minimum and maximum values.
- Calculating the range of a sequence.
- Calculating the sum of a sequence.
- Converting Celsius to Fahrenheit.
- Calculating the arithmetic mean of two or more numerical values.

Some functions may build upon other functions in your library.

For example, the range function can use the minimum and maximum functions rather than repeating their calculation logic.

### Input and error handling

Consider how your functions should behave when:

- The input sequence is empty.
- The input contains non-numeric values.
- The input contains negative numbers.
- The input contains only one number.
- A function receives an unexpected argument.

Choose and document a consistent behavior for invalid inputs. You do not need to implement every possible form of validation, but your choices should be intentional.

## 5. Recommended Project Structure

Organize your files as follows:

```text
project-008/
├── main.py
├── calculations.py
└── README.md
```

### File responsibilities

**`calculations.py`**

Contains your reusable calculation functions.

This file should focus on computation rather than displaying the final report.

**`main.py`**

Imports functions from `calculations.py`, supplies sample inputs, calls the functions, and displays the results.

**`README.md`**

Documents the project's objective, implementation, usage, and lessons learned.

Keep the implementation in `calculations.py` and the demonstration code in `main.py` separate.

## 6. Tasks and Milestones

### Task 1: Review previous calculations

Review the calculation functions you implemented in earlier projects.

Identify which calculations are useful enough to reuse in multiple programs.

Write down the expected inputs and outputs for each function before coding.

### Task 2: Create the calculation module

Create `calculations.py`.

Implement the required numerical functions using clear names and appropriate parameters.

Each function should return its calculated result rather than printing it directly.

### Task 3: Add docstrings

Write a short docstring for every public function.

Each docstring should explain:

- What the function does.
- What inputs it expects.
- What it returns.
- Any important restrictions or assumptions.

Use descriptive parameter names and keep each function focused on one responsibility.

### Task 4: Import functions into the main program

Create `main.py`.

Import the functions you need from `calculations.py` and call them using sample numerical data.

Display the results in a readable report.

Verify that the module can be imported successfully when both files are in the same directory.

### Task 5: Test multiple inputs

Test your functions with several different input sequences.

Include:

- A sequence of positive numbers.
- A sequence containing negative numbers.
- A sequence containing a single number.
- An empty sequence.
- An invalid input, where relevant.

Check whether the results match your expectations.

### Task 6: Improve reusability

Review your implementation.

Look for duplicated calculations and determine whether one function can reuse another.

Make sure that changing the input data does not require rewriting the calculation logic.

### Task 7: Document and review

Update this README with a brief explanation of your implementation and any important design decisions.

Record the tests you performed and any limitations you identified.

## 7. Expected Output

Your program should produce a readable report similar to the following:

```text
REUSABLE CALCULATION LIBRARY
================================
Input values: [10, 20, 30, 40, 50]

Sum: 150
Mean: 30.0
Minimum: 10
Maximum: 50
Range: 40

Temperature Conversion
----------------------
Celsius: 25
Fahrenheit: 77.0
```

Your formatting and implementation may differ, provided that the calculations are correct and the output is understandable.

## 8. Success Criteria

The project is complete when:

- [ ] All required calculation functions are implemented.
- [ ] Functions accept parameters and return appropriate results.
- [ ] Functions include meaningful docstrings.
- [ ] Calculation logic is stored in `calculations.py`.
- [ ] `main.py` imports and uses the calculation functions successfully.
- [ ] The same functions work with different valid inputs.
- [ ] Empty or invalid inputs are handled according to documented rules.
- [ ] Duplicated calculation logic has been minimized.
- [ ] The output is clearly formatted.
- [ ] The README explains how to run the program and what it demonstrates.

## 9. How to Run the Project

Open a terminal in the `project-008` directory.

Run:

```bash
python main.py
```

If Python is configured correctly, the main program should import your module, execute the calculations, and display the report.

You do not need to install any external packages for this project.

## 10. MATLAB vs. Python

In MATLAB, you may define functions in separate `.m` files and call them from other scripts or functions.

Python provides a similar capability through modules.

For example, a Python file named `calculations.py` can be imported by another file using:

```python
from calculations import calculate_mean
```

The imported function can then be called using its name and appropriate arguments.

Important differences:

- Python module names are based on filenames, without the `.py` extension in an import statement.
- Python uses indentation to define function bodies.
- Python functions use `return` to send results back to their callers.
- Python's import system makes it straightforward to organize related functions into reusable modules and packages.

## 11. Extension Challenges

Complete these challenges after the core requirements work.

### Challenge 1: Add standard deviation

Add a function that calculates the population standard deviation of a numerical sequence.

Use the `statistics` module or implement the calculation yourself, and clearly document which approach you chose.

### Challenge 2: Add unit conversions

Extend the library with conversions for kilometers to miles and kilograms to pounds.

Use descriptive function names and consistent input/output conventions.

### Challenge 3: Add automated tests

Create a separate test file and use Python's built-in `unittest` framework to test your functions.

Test both expected numerical results and invalid inputs.

### Challenge 4: Reuse the library in another program

Create a second demonstration script that imports the same calculation module.

Use a different set of inputs without modifying `calculations.py`.

This demonstrates that your library is genuinely reusable.

## 12. Reflection Questions

After completing the project, answer these questions in your own words:

1. What is the difference between printing a value and returning a value?
2. Why is it useful to store calculation functions in a separate module?
3. What happens when you import a function from another Python file?
4. How does Python's module system compare with MATLAB function files?
5. Which functions reuse other functions, and why?
6. How did you decide what should happen when a function receives an empty sequence?
7. What would you change if this library needed to support hundreds of calculations?

## 13. GitHub Deliverables

Your repository should contain:

- `calculations.py`
- `main.py`
- `README.md`

If you complete the extension challenges, include your test file as well.

Before committing, run the program and verify that the documented execution steps work.

Suggested commit message:

```text
Add reusable Python calculation library
```

## 14. Key Takeaway

This project marks an important transition from writing individual Python programs to designing reusable components.

A well-designed function should have a clear responsibility, accept appropriate inputs, return predictable results, and be easy to test.

These habits will become increasingly important as you move toward NumPy, pandas, exploratory data analysis, and larger analytical projects.

**Focus on understanding how to organize and reuse your code—not on writing the largest possible library.**