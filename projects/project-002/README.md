# Project 002: Unit Conversion Toolkit

**Difficulty:** Beginner  
**Estimated Time:** 1–2 hours  
**Language:** Python 3  
**Libraries:** Python Standard Library  
**Status:** Not Started

## 1. Project Overview

The Unit Conversion Toolkit is a Python program that converts numerical values between commonly used measurement units.

The goal is to practice writing reusable functions, handling numerical inputs, and organizing calculation logic into a simple, understandable program.

This project is part of my **100 Python Data Analytics Projects** learning roadmap. It builds on Project 001 by moving from individual arithmetic calculations to a collection of reusable conversion functions.

## 2. Learning Objectives

By completing this project, I aim to learn how to:

- Define and reuse Python functions.
- Pass arguments to functions and return calculated values.
- Work with floating-point numbers.
- Apply mathematical conversion formulas.
- Format numerical results using f-strings.
- Validate inputs and handle invalid values.
- Organize related functions in a Python script.
- Test functions with different inputs.

## 3. Project Requirements

### Task 1: Length Conversion

Implement conversions between the following units:

- Meters to kilometers
- Kilometers to meters
- Meters to centimeters
- Centimeters to meters

Use these relationships:

- 1 kilometer = 1,000 meters
- 1 meter = 100 centimeters

### Task 2: Temperature Conversion

Implement conversions between:

- Celsius and Fahrenheit
- Fahrenheit and Celsius

Use the formulas:

\[
F = \frac{9}{5}C + 32
\]

\[
C = \frac{5}{9}(F - 32)
\]

### Task 3: Pressure Conversion

Implement conversions between:

- Pascals and kilopascals
- Kilopascals and Pascals

Use the relationship:

- 1 kilopascal = 1,000 pascals

### Task 4: Create Reusable Functions

Create a separate function for each conversion direction.

Each function should:

1. Accept a numerical value as an argument.
2. Perform the appropriate conversion.
3. Return the converted value.
4. Avoid printing results directly inside the conversion function.

The main program should be responsible for displaying the results.

### Task 5: Display Conversion Results

Print a clearly formatted report containing:

- The original value and unit.
- The converted value and unit.
- A descriptive label for each conversion.

Use consistent numerical formatting and make the units explicit.

### Task 6: Test the Conversions

Test the functions with:

- Positive values.
- Decimal values.
- Zero.
- Negative temperatures.
- Values that convert to exact results.
- Values that require decimal precision.

Check that the results match the expected mathematical relationships.

## 4. Example Output

The following is an example of the intended output format. Your program does not need to match it exactly.

```text
UNIT CONVERSION TOOLKIT
--------------------------------
Length:
1.50 km = 1500.00 m
250.00 cm = 2.50 m

Temperature:
25.00 °C = 77.00 °F
32.00 °F = 0.00 °C

Pressure:
101325.00 Pa = 101.325 kPa
100.00 kPa = 100000.00 Pa
```

## 5. Project Structure

```text
project-002/
├── main.py
└── README.md
```

- `main.py`: Contains the conversion functions and report generation.
- `README.md`: Documents the project's objectives, requirements, instructions, and results.

## 6. How to Run

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Run the program from the integrated terminal.

```bash
python main.py
```

No third-party libraries are required.

## 7. Success Criteria

The project is complete when:

- [ ] Length conversions produce correct results.
- [ ] Temperature conversions produce correct results.
- [ ] Pressure conversions produce correct results.
- [ ] Each conversion is implemented as a reusable function.
- [ ] Functions return results rather than printing them directly.
- [ ] The program displays clear labels and units.
- [ ] Decimal values are handled correctly.
- [ ] The code is readable and logically organized.
- [ ] The README explains how to run the program.

## 8. MATLAB-to-Python Lessons

This project reinforces several differences between MATLAB and Python.

| Concept | MATLAB | Python |
|---|---|---|
| Function definition | `function y = f(x)` | `def f(x):` |
| Return a value | Assign output variable | Use `return` |
| Function calls | `f(x)` | `f(x)` |
| Multiple functions | Often separate function files or local functions | Multiple functions can be defined in one module |
| Display output | `disp()` or `fprintf()` | `print()` and f-strings |
| Code blocks | `end` | Indentation |

One important design principle is to separate **calculation logic** from **presentation logic**. Conversion functions should calculate and return values; the main program should decide how to display them.

## 9. Future Improvements

After completing the required tasks, consider these extensions:

- Allow users to choose a conversion interactively.
- Let users enter a value rather than hard-code it.
- Add mass, speed, energy, and volume conversions.
- Create a dictionary to organize supported conversion options.
- Add input validation and informative error messages.
- Write automated tests using Python's `unittest` module.

Implement these improvements only after the basic version works correctly.

## 10. Learning Reflection

Complete this section after implementing and testing the program.

- **What I learned:** _To be completed._
- **What was difficult:** _To be completed._
- **What errors I encountered and how I fixed them:** _To be completed._
- **What I can now explain without assistance:** _To be completed._
- **What I would improve in a second version:** _To be completed._

---

**Repository:** Python Data Analyst — 100 Projects  
**Project:** 002 / 100  
**Previous project:** Numerical Calculator for Engineers  
**Next project:** Statistical Summary Calculator