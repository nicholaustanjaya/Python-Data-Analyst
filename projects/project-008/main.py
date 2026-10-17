import calculations

def main():
    # Sample inputs
    numbers = [10, 20, 30, 40, 50]
    celsius = 25

    # Calculate mean
    mean = calculations.calculate_mean(numbers)
    print(f"Mean: {mean}")

    # Find min and max
    min_value = calculations.find_min(numbers)
    max_value = calculations.find_max(numbers)
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")

    # Calculate range
    range_value = calculations.calculate_range(numbers)
    print(f"Range: {range_value}")

    # Calculate sum
    sum_value = calculations.calculate_sum(numbers)
    print(f"Sum: {sum_value}")

    # Convert Celsius to Fahrenheit
    fahrenheit = calculations.celsius_to_fahrenheit(celsius)
    print(f"Fahrenheit: {fahrenheit}")

    # Arithmetic mean
    mean_two_numbers = calculations.arithmetic_mean(10, 20)
    print(f"Arithmetic Mean of 10 and 20: {mean_two_numbers}")

if __name__ == "__main__":
    main()