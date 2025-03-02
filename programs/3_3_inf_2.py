def digit_sum(n):
    """Efficiently compute the sum of digits of a number using integer arithmetic."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def get_difference(numbers):
    # Initialize smallest and largest to None
    smallest = None
    largest = None

    # Iterate over each number in the list
    for number in numbers:
        # Check if the sum of digits is 30
        if digit_sum(number) == 30:
            # Update smallest and largest as needed
            if smallest is None or number < smallest:
                smallest = number
            if largest is None or number > largest:
                largest = number

    # If no valid numbers were found, return 0
    if smallest is None or largest is None:
        return 0

    # Return the difference
    return largest - smallest


# Example usage (with smaller numbers for demonstration purposes):
# import random
# numbers = [random.randint(1, 100000) for _ in range(1000000)]
# print(get_difference(numbers))
