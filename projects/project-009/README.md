# Project 9: Command-Line Data Summary

## 1. Project Overview

**Difficulty:** Beginner  
**Estimated Time:** 2–3 hours  
**Primary Language:** Python  
**External Libraries:** None (Python standard library only)

### Objective

Build a command-line Python program that reads a collection of numerical values and produces a summary report.

The program should demonstrate how to organize calculations into functions, structure a Python script, and provide useful output through the command line.

This project is an important step toward building reusable data analysis tools before introducing NumPy and pandas.

## 2. Learning Objectives

By completing this project, I will learn how to:

- Organize Python code into multiple functions.
- Separate calculation logic from input/output operations.
- Use Python modules and imports.
- Understand the `if __name__ == "__main__":` pattern.
- Accept input through command-line arguments or a simple input prompt.
- Calculate basic descriptive statistics.
- Validate numerical inputs and handle errors.
- Format readable command-line reports.
- Write maintainable Python code that can be extended in future projects.

## 3. Project Requirements

Create a Python program that summarizes numerical measurements.

### Required Features

1. Accept a collection of numerical values.
2. Calculate the number of observations.
3. Calculate the sum, mean, minimum, maximum, and range.
4. Display the results in a readable report.
5. Handle invalid input gracefully.
6. Handle an empty dataset without crashing.
7. Handle a dataset containing a single observation.
8. Handle division by zero or other invalid numerical operations where applicable.

### Example Input

```text
10, 20, 30, 40, 50
```

### Example Output

```text
================================
       DATA SUMMARY REPORT
================================

Number of observations: 5
Sum:                   150.00
Mean:                   30.00
Minimum:                10.00
Maximum:                50.00
Range:                  40.00

================================
```

The exact formatting may differ, provided that all required statistics are correct and clearly labeled.

## 4. Technical Requirements

Use only Python's standard library and built-in capabilities.

Recommended concepts:

- Variables and data types
- Lists and loops
- Functions and return values
- `sum()`, `min()`, and `max()`
- Conditional statements
- Exception handling with `try` and `except`
- String methods such as `split()`
- String formatting with f-strings
- The `if __name__ == "__main__":` entry-point pattern

Do not use NumPy or pandas yet. The purpose is to strengthen your understanding of core Python before moving to specialized data analysis libraries.

## 5. Suggested Project Structure

```text
project-009/
├── main.py
└── README.md
```

Keep the project simple. Additional modules and test files can be introduced if they improve your implementation.

## 6. Implementation Milestones

### Milestone 1: Accept Numerical Input

- Accept multiple numerical values from the user.
- Convert the input strings into numeric values.
- Store the values in a list.
- Detect invalid input.

### Milestone 2: Create a Statistics Function

Create a function that receives a list of numbers and calculates the required statistics.

The function should return its results rather than print them directly.

### Milestone 3: Create a Report Function

Create a separate function responsible for displaying the summary.

Keep the calculations separate from presentation logic.

### Milestone 4: Handle Edge Cases

Test the following scenarios:

- Several positive numbers
- Positive and negative numbers
- Decimal values
- A single number
- Empty input
- Invalid text input
- A mixture of valid and invalid values

Decide whether invalid input should be rejected entirely or whether the program should ask the user to correct it.

Document your decision.

### Milestone 5: Add the Main Entry Point

Organize the program so that the main workflow runs through a dedicated function or entry-point block.

The program should also be importable from another Python file without automatically executing its interactive workflow.

### Milestone 6: Validate and Document

- Run all test cases.
- Verify calculations independently.
- Review variable and function names.
- Confirm that the output is readable.
- Update this README if the implementation differs from the planned behavior.

## 7. Success Criteria

The project is complete when:

- [ ] The program accepts multiple numerical values.
- [ ] The program calculates all required statistics correctly.
- [ ] Calculation logic is separated into functions.
- [ ] The report is readable and consistently formatted.
- [ ] Invalid input is handled intentionally.
- [ ] Empty and single-value datasets are handled correctly.
- [ ] The main entry point follows standard Python conventions.
- [ ] The program runs from the VS Code terminal.
- [ ] The code contains meaningful names and appropriate comments.
- [ ] I can explain the purpose of each function without relying on the README or an AI-generated explanation.

## 8. Example Test Cases

| Input | Expected Result |
|---|---|
| `10,20,30` | Mean = 20, minimum = 10, maximum = 30, range = 20 |
| `-5,0,5` | Mean = 0, minimum = -5, maximum = 5, range = 10 |
| `2.5,3.5` | Mean = 3, minimum = 2.5, maximum = 3.5, range = 1 |
| `7` | Mean = minimum = maximum = 7, range = 0 |
| Empty input | Display a clear message or request valid input |
| `10,abc,30` | Report an understandable input error or request correction |

## 9. Running the Program

Open the project directory in VS Code.

Activate your Python virtual environment if you are using one, then run:

```bash
python main.py
```

Follow the program's input instructions.

## 10. Portfolio Value

**Portfolio category:** Foundational practice project

This is primarily a learning exercise rather than a standalone flagship portfolio project.

It demonstrates fundamental Python programming, input validation, function design, and command-line interaction.

These skills will be reused in later projects involving CSV files, pandas, automated reports, and reusable analytics pipelines.

## 11. Extension Challenges

After completing the required features, choose one or more extensions:

1. **Standard deviation:** Calculate population and sample standard deviations using the `statistics` module.
2. **File input:** Read numerical values from a CSV file.
3. **Command-line arguments:** Use `argparse` to accept a filename or numerical values directly from the terminal.
4. **JSON output:** Export the summary report to a JSON file.
5. **Unit tests:** Write tests using Python's `unittest` module.
6. **Reusable module:** Move the statistics functions into a separate Python module and import them into `main.py`.

Complete the required version before attempting the extensions.

## 12. Reflection

After completing the project, answer these questions:

1. Why is it useful to separate calculations from report formatting?
2. Why should a function return a result instead of always printing it?
3. What is the purpose of `if __name__ == "__main__":`?
4. How does Python's list behavior differ from a MATLAB numeric array?
5. Which edge case required the most careful handling?
6. What would need to change if the input contained one million measurements?

## 13. Final Notes

The goal is not simply to produce the correct output. The goal is to build a program that is understandable, testable, and easy to extend.

Complete the project independently, validate the results, and record what you learned before moving to Project 10: CSV Measurement Reader.