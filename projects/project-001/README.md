# Project 001: Numerical Calculator for Engineers

**Difficulty:** Beginner  
**Estimated Time:** 1–2 hours  
**Language:** Python 3  
**Libraries:** Python Standard Library  
**Status:** In Progress

## 1. Project Overview

The Numerical Calculator for Engineers is a beginner-friendly Python project designed to practice fundamental programming concepts through simple engineering calculations.

The program performs arithmetic operations on two numerical values, converts temperatures from Celsius to Fahrenheit, and presents the results in a clear, readable report.

This project is part of my **100 Python Data Analytics Projects** learning roadmap. My goal is to transition from MATLAB programming to Python and gradually develop the skills required for practical data analysis.

## 2. Learning Objectives

By completing this project, I aim to learn how to:

- Declare variables and work with numeric data types.
- Perform arithmetic calculations in Python.
- Define and call functions.
- Accept and process function arguments.
- Return calculated values from functions.
- Format numerical output using Python f-strings.
- Handle division by zero and invalid inputs.
- Write readable, maintainable Python code.
- Run and debug Python scripts in VS Code.

## 3. Project Requirements

### Task 1: Define Numerical Inputs

Define two numerical variables:

- `value_a = 12.5`
- `value_b = 4.0`

These values represent example engineering measurements.

### Task 2: Perform Arithmetic Operations

Calculate the following:

- Sum
- Difference
- Product
- Average
- Ratio of the first value to the second value

Handle division by zero intentionally.

### Task 3: Convert Temperature

Create a reusable function that converts Celsius to Fahrenheit using:

\[
F = \frac{9}{5}C + 32
\]

The function should accept a Celsius temperature and return the corresponding Fahrenheit temperature.

### Task 4: Generate a Calculation Report

Display the input values and calculated results in a clearly labeled report.

Format numerical values consistently and use descriptive labels so the output is easy to understand.

### Task 5: Test the Program

Test the program using:

- Positive numerical values.
- Decimal values.
- Negative values.
- Zero as a calculation input.
- Zero as the denominator of a division.
- Invalid input, where applicable.

Confirm that the program behaves as expected.

## 4. Expected Output

The program should produce a report similar to the following:

```text
ENGINEERING CALCULATION REPORT
--------------------------------
Value A:       12.50
Value B:        4.00
Sum:           16.50
Difference:     8.50
Product:       50.00
Average:        8.25
Ratio A / B:    3.125
```

A Celsius-to-Fahrenheit conversion result should also be displayed.

The final output may differ slightly depending on the implementation.

## 5. Project Structure

```text
project-001/
├── main.py
└── README.md
```

- `main.py`: Contains the calculation logic and report generation.
- `README.md`: Documents the project's purpose, requirements, execution instructions, and results.

## 6. How to Run

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Run the script using the Python extension or the integrated terminal.

From the terminal, execute:

```bash
python main.py
```

If your system uses a different Python command, use the command associated with your installation.

## 7. Success Criteria

The project is complete when:

- [ ] The program executes without syntax errors.
- [ ] All arithmetic calculations produce the expected results.
- [ ] The temperature conversion is implemented as a reusable function.
- [ ] Division by zero is handled intentionally.
- [ ] Numerical results are clearly labeled and consistently formatted.
- [ ] Invalid inputs are handled appropriately for the chosen input method.
- [ ] The code is readable and logically organized.
- [ ] The README explains the project and how to run it.

## 8. MATLAB-to-Python Lessons

This project introduces several differences between MATLAB and Python.

| Concept | MATLAB | Python |
|---|---|---|
| Variable assignment | `x = 10;` | `x = 10` |
| Function definition | `function y = f(x)` | `def f(x):` |
| Function return | `y = ...` | `return ...` |
| Code blocks | `end` | Indentation |
| String formatting | `sprintf()` | f-strings |
| Script execution | Run a script or section | Run a `.py` file |

One important distinction is that Python uses indentation to define code blocks. Consistent indentation is therefore essential.

## 9. Future Improvements

After completing the basic requirements, possible extensions include:

- Accept numerical inputs interactively.
- Add unit conversions for length, pressure, and other physical quantities.
- Support multiple calculations in one execution.
- Add more robust input validation.
- Separate the calculation functions from report generation.
- Add automated tests using `pytest`.

These improvements should be implemented gradually as new concepts are learned.

## 10. Key Takeaways

After finishing this project, I should be able to explain:

1. How Python performs basic numerical calculations.
2. How functions receive arguments and return values.
3. How to format numerical results for readable output.
4. How to identify and handle simple edge cases.
5. How Python differs from MATLAB in function definitions and code structure.

## 11. Learning Reflection

Complete this section after implementing the project.

- **What I learned:** _To be completed._
- **What was difficult:** _To be completed._
- **What errors I encountered and how I fixed them:** _To be completed._
- **What I can now explain without assistance:** _To be completed._
- **What I would improve in a second version:** _To be completed._

---

**Repository:** Python Data Analyst — 100 Projects  
**Project:** 001 / 100  
**Next project:** Unit Conversion Toolkit