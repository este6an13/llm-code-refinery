def get_difference(numbers):
    """Finds the difference between the smallest and largest numbers
    in a list whose digits sum up to 30."""

    min_number = None
    max_number = None

    for number in numbers:
        digit_sum = 0
        n = number

        # Calculate digit sum
        while n > 0:
            digit_sum += n % 10
            if digit_sum > 30:  # Early exit if digit sum exceeds 30
                break
            n //= 10

        # Check if the sum of digits equals 30
        if digit_sum == 30:
            if min_number is None or number < min_number:
                min_number = number
            if max_number is None or number > max_number:
                max_number = number

    # If no numbers found with digit sum 30, return 0
    if min_number is None or max_number is None:
        return 0

    return max_number - min_number


# Example usage:
import random

# Generate a list of 1 million random integers between 1 and 100000
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Get the difference between the smallest and largest numbers whose digits sum up to 30
difference = get_difference(random_numbers)

print("The difference is:", difference)
