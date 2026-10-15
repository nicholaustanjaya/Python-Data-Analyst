# Project 006: Measurement Quality Checker

**Difficulty:** Beginner\
**Estimated time:** 2 hours\
**Primary skills:** Variables, lists, conditionals, Boolean logic,
loops, functions (optional), input validation\
**Dependencies:** Python 3 standard library only\
**Dataset:** Synthetic sensor readings created directly in the script

## 1. Project Overview

In engineering and data analysis, measurements are not automatically
trustworthy. A sensor may report values outside its expected operating
range because of noise, faults, incorrect configuration, or data-entry
mistakes.

In this project, build a small Python program that checks a collection
of synthetic sensor readings against acceptable limits and reports which
readings are valid, too low, or too high.

This is a practice project: focus on clear logic, correct boundary
handling, and understandable output rather than advanced statistics or
external libraries.

## 2. Learning Objectives

By completing this project, you should be able to:

-   Use `if`, `elif`, and `else` to implement decision logic.
-   Combine comparisons with Boolean logic.
-   Iterate through a list of measurements.
-   Distinguish values below, within, and above an acceptable range.
-   Handle boundary values consistently.
-   Produce a readable validation report.
-   Explain how Python comparisons and indexing differ from MATLAB.

## 3. Scenario

Imagine that a temperature sensor is expected to report values between
**15.0 °C and 30.0 °C, inclusive**.

Your program receives a list of readings, for example:

``` python
readings = [22.5, 14.2, 30.0, 31.7, 18.9, 15.0, -2.0, 27.3]
```

For each reading, classify it as one of the following:

-   `TOO LOW`: the reading is below the minimum limit.
-   `VALID`: the reading is within the allowed range, including both
    limits.
-   `TOO HIGH`: the reading is above the maximum limit.

The limits should be stored in variables rather than repeated as
unexplained numbers throughout the program.

## 4. Requirements

Create the project in this folder:

``` text
projects/
└── project-006/
    ├── main.py
    └── README.md
```

Your program should:

1.  Define a list of synthetic sensor readings.
2.  Define the minimum and maximum acceptable values.
3.  Inspect every reading.
4.  Classify each reading using conditional statements.
5.  Print each reading with its classification and unit.
6.  Count the total number of valid, too-low, and too-high readings.
7.  Print a summary containing the total number of readings and the
    count in each category.
8.  Keep the code readable with descriptive variable names.

Do not use NumPy or pandas for this project. The goal is to practice
Python fundamentals.

## 5. Implementation Milestones

### Milestone 1 --- Define the data and limits

Create the readings list and variables for the lower and upper limits.
Choose names that make the meaning and units clear.

### Milestone 2 --- Write the decision logic

For a single reading, determine which condition applies:

-   Is it less than the minimum?
-   Otherwise, is it greater than the maximum?
-   Otherwise, it is valid.

Think carefully about why the final `else` covers the valid range.

### Milestone 3 --- Process all readings

Use a loop to apply the classification to every reading. Avoid writing a
separate set of conditions for each individual value.

### Milestone 4 --- Count classifications

Maintain counters for valid, too-low, and too-high readings. Update
exactly one counter for each measurement.

### Milestone 5 --- Print a readable report

Include the limits, each measurement and its status, and a final
summary. Use consistent formatting and include the unit `°C`.

### Milestone 6 --- Test edge cases

Use the test cases in Section 7. Fix any boundary or counting errors you
discover.

## 6. MATLAB-to-Python Notes

### Conditional statements

MATLAB:

``` matlab
if value < lower_limit
    status = "TOO LOW";
elseif value > upper_limit
    status = "TOO HIGH";
else
    status = "VALID";
end
```

Python:

``` python
if value < lower_limit:
    status = "TOO LOW"
elif value > upper_limit:
    status = "TOO HIGH"
else:
    status = "VALID"
```

Python uses a colon (`:`) and indentation to define a block instead of
MATLAB's `end`.

### Logical operators

  Meaning        MATLAB                     Python
  -------------- -------------------------- --------
  Logical AND    `&&` (scalar conditions)   `and`
  Logical OR     `||` (scalar conditions)   `or`
  Logical NOT    `~`                        `not`
  Equal to       `==`                       `==`
  Not equal to   `~=`                       `!=`

For this project, use simple comparisons and `if`/`elif`/`else` first.
Python's `and` and `or` are intended for scalar Boolean logic; NumPy
arrays use different elementwise operators, which you will learn later.

### Indexing

Python lists start at index `0`, unlike MATLAB arrays, which start at
index `1`. You do not need indexing to classify each reading if you loop
directly over the values.

## 7. Manual Test Cases

Check that your program handles the following values when the acceptable
range is 15.0--30.0 °C.

    Reading Expected classification   Reason
  --------- ------------------------- --------------------
     `14.9` `TOO LOW`                 Below minimum
     `15.0` `VALID`                   Exactly at minimum
     `22.5` `VALID`                   Within range
     `30.0` `VALID`                   Exactly at maximum
     `30.1` `TOO HIGH`                Above maximum
     `-2.0` `TOO LOW`                 Below minimum

Also test a list where every value is valid, a list where every value is
too low or too high, and an empty list. Decide what the summary should
report for an empty list; it should not crash.

## 8. Expected Output Format

Your exact wording can differ, but aim for output similar to this:

``` text
MEASUREMENT QUALITY REPORT
Acceptable range: 15.0 °C to 30.0 °C
-------------------------------------
Reading: 22.5 °C | Status: VALID
Reading: 14.2 °C | Status: TOO LOW
Reading: 30.0 °C | Status: VALID
Reading: 31.7 °C | Status: TOO HIGH

SUMMARY
Total readings: 4
Valid: 2
Too low: 1
Too high: 1
```

The values above are illustrative. Your report should reflect the full
list you actually process.

## 9. Success Criteria

-   [ ] The program runs without syntax errors.
-   [ ] Every reading receives exactly one classification.
-   [ ] Values equal to either limit are classified as valid.
-   [ ] Values below and above the limits are classified correctly.
-   [ ] The counters match the classifications shown in the report.
-   [ ] The output includes units and clear labels.
-   [ ] An empty readings list does not cause a crash.
-   [ ] The code uses descriptive variable names and consistent
    indentation.
-   [ ] You can explain the conditions without reading from a tutorial.

## 10. Extension Challenges

Complete these only after the basic requirements work.

1.  **Reusable function:** Write a function that accepts one reading and
    the two limits, then returns its classification.
2.  **Percentage summary:** Calculate the percentage of readings that
    are valid. Handle an empty list without dividing by zero.
3.  **Multiple sensors:** Check temperature and pressure readings using
    different limits.
4.  **Input validation:** Investigate what happens if a reading is a
    string instead of a number. Decide how your program should handle
    invalid input.
5.  **Quality threshold:** Print a warning if the percentage of invalid
    readings exceeds a threshold you choose.

## 11. Reflection Questions

Answer these in your notes or at the end of your project README:

1.  Why should the lower and upper limits be stored in variables?
2.  Why is `elif` appropriate for this classification?
3.  What happens if you accidentally use `value <= lower_limit` for the
    `TOO LOW` condition?
4.  How do you know that every reading is counted exactly once?
5.  What additional checks would be necessary before using this logic
    with real sensor data?

## 12. How to Run

From the project directory, run:

``` bash
python main.py
```

No third-party packages are required.

## 13. Definition of Done

The project is complete when the program classifies the readings
correctly, passes the manual boundary tests, prints an accurate summary,
and you can explain the logic in your own words.

**Mentor rule:** Attempt the implementation before looking for a
complete solution. If something fails, inspect the error message, test
one reading at a time, and verify the boundary cases first.
