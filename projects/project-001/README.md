Project 001: Numerical Calculator for Engineers
B — Beginner
1–2 hours
Python standard library only

Objective
Create a Python program that performs basic numerical calculations and prints a clean, readable report. Use an engineering-oriented example rather than a generic calculator with buttons.
Problem statement: Given two measurements, calculate their sum, difference, product, ratio and average. Add a temperature conversion as a separate function. The program should clearly identify units and handle invalid inputs.

Tasks and milestones
1. Create the script. Create a folder named project-001 and a file named main.py. Run a simple print() statement from VS Code.
2. Define variables. Store two numeric measurements, such as value_a = 12.5 and value_b = 4.0.
3. Perform calculations. Calculate the sum, difference, product, average and ratio. Decide what should happen if the second value is zero.
4. Write a function. Create a function that converts Celsius to Fahrenheit. It should accept a number and return the converted value.
5. Format a report. Print each calculation with a descriptive label and sensible numerical formatting.
6. Test edge cases. Check negative values, decimal values, zero, and an invalid input such as a text string where a number is expected.
7. Document your work. Write a short README with the objective, how to run the program, example input/output and one limitation.

Expected output
A possible report format is shown below. Your implementation and wording can differ.
ENGINEERING CALCULATION REPORT
--------------------------------
Value A:       12.50
Value B:        4.00
Sum:           16.50
Difference:     8.50
Product:       50.00
Average:        8.25
Ratio A / B:    3.125


The report should also show the Celsius-to-Fahrenheit conversion when you complete that task.

Success criteria
[ ] The script runs from VS Code without syntax errors.
[ ] All calculations produce the expected numerical results.
[ ] The temperature conversion is implemented as a function that returns a value.
[ ] Division by zero is handled intentionally.
[ ] Numeric output is clearly labeled and formatted.
[ ] The README explains how to run the script.
0 of 6 completion criteria checked.

Hints — use these before asking for a solution
Hint 1: Basic arithmetic
Python uses +, -, *, /, and ** for addition, subtraction, multiplication, division and exponentiation. Parentheses work as expected.
Hint 2: Functions
A Python function starts with def. It can receive arguments and return a result. Unlike a MATLAB function file, Python relies on indentation to define its body.
Hint 3: Temperature conversion
The relationship is:
\[
F = \frac{9}{5}C + 32
\]

Try implementing the formula yourself, using a function that accepts a Celsius value and returns a Fahrenheit value.
Hint 4: Invalid division
Use a conditional statement to check whether the denominator is zero before dividing. Later, you can explore exceptions for more general error handling.
Hint 5: Clean output
Python f-strings let you insert values into text. For example, f"{value:.2f}" formats a number to two decimal places.
What I want you to do now
Do not ask for the complete solution yet. Write your own main.py, run it, and bring back your code—even if it does not work.
I'll review it for correctness, readability, Python conventions, and MATLAB-related mistakes. We'll fix the problems together, then move to Project 2 once you can explain your implementation.
Your first objective is not to write perfect Python. It is to write a working program, understand why it works, and know how to verify it. 🚀