def calculate_mean(sequence):
    """Calculate the mean of a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    float: The mean of the sequence.
    """
    if not sequence:
        raise ValueError("The sequence is empty.")
    return sum(sequence) / len(sequence)

def find_min(sequence):
    """Find the minimum value in a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    float: The minimum value in the sequence.
    """
    if not sequence:
        raise ValueError("The sequence is empty.")
    return min(sequence)

def find_max(sequence):
    """Find the maximum value in a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    float: The maximum value in the sequence.
    """
    if not sequence:
        raise ValueError("The sequence is empty.")
    return max(sequence)

def calculate_range(sequence):
    """Calculate the range of a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    float: The range of the sequence.
    """
    if not sequence:
        raise ValueError("The sequence is empty.")
    return find_max(sequence) - find_min(sequence)

def calculate_sum(sequence):
    """Calculate the sum of a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    float: The sum of the sequence.
    """
    return sum(sequence)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def arithmetic_mean(*args):
    """Calculate the arithmetic mean of two or more numerical values.

    Parameters:
    *args (float): A variable number of numbers.

    Returns:
    float: The arithmetic mean of the numbers.
    """
    if not args:
        raise ValueError("No numbers provided.")
    return sum(args) / len(args)