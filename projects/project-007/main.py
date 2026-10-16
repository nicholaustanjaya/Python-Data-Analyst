# Task 1
# Define simulation parameters

REFERENCE_VALUE = 25
NUMBER_OF_MEASUREMENTS = 100 
STANDARD_DEVIATION = 0.5
RANDOM_SEED = 10

# Task 2
# Generate random noise
import random

random.seed(RANDOM_SEED)
noise = [random.gauss(0, STANDARD_DEVIATION) for _ in range(NUMBER_OF_MEASUREMENTS)]

# Task 3 & 4
# Create measurement simulation function
# Generate repeated measurements

def simulate_measurements(reference_value, noise):
    measurements = [reference_value + n for n in noise]
    return measurements

# Task 5
# Calculate summary statistics
def calculate_statistics(measurements):
    mean = sum(measurements) / len(measurements)
    minimum = min(measurements)
    maximum = max(measurements)
    range_value = maximum - minimum
    return mean, minimum, maximum, range_value

statistics = calculate_statistics(simulate_measurements(REFERENCE_VALUE, noise))

# Task 6
# export the measurements measurements.csv
import csv

with open ('measurements.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Measurement'])
    for measurement in simulate_measurements(REFERENCE_VALUE, noise):
        writer.writerow([measurement])
    writer.writerow(["Mean", statistics[0]])
    writer.writerow(["Minimum", statistics[1]])
    writer.writerow(["Maximum", statistics[2]])
    writer.writerow(["Range", statistics[3]])
    
    





