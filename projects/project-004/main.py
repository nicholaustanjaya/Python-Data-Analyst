# Task 1
# create the data
temperatures = [21.5, 22.0, 21.8, 23.1, 22.7]

# print entire list
print(temperatures)

# print the number of measurement
N = len(temperatures)

# Print first and last measurement
print(f"First measurement : {temperatures[0]}, Last measurement : {temperatures[-1]}")

# Task 2
# access individual element
first = temperatures[0]
third = temperatures[2]
last = temperatures[-1]
second_to_last = temperatures[-2]

# Task 3
first_three_measurements = temperatures[0:2]
second_to_fourth = temperatures[1:3]
all_ex_first_n_last = temperatures[1:-2]
last_three_measurements = temperatures[-3]