# Task 1
# Declare variables
value_a = 12.5
value_b = 4.0

# Task 2
# Sum
value_sum = value_a + value_b

# Difference
value_difference = value_a - value_b

# Product
value_product = value_a * value_b

# Average
value_average = 0.5 * (value_a + value_b)

# Ratio of the first value to the second value
try:
    value_division = value_a / value_b
except ZeroDivisionError:
    print("You can't divide by zero, value_b can't be zero")

# Task 3
# Convert Celsius to Fahrenheit
def CtoF(degreeC):
    degreeF = 9/5 * degreeC + 32 
    return degreeF

# Task 4
# Generate Calculation Report
print(f"""ENGINEERING CALCULATION REPORT
-------------------------------------
Value A: {value_a:.2f}
Value B: {value_b:.2f}
Sum: {value_sum:.2f}
Difference: {value_difference:.2f}
Product: {value_product:.2f}
Average: {value_average:.2f}
Ratio A / B: {value_division:.2f}
Temperature in degF: {CtoF(100)} degF""")

# Task 5
# Test the program
assert value_sum == 16.5