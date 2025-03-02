def get_difference(numbers):
    min_num = float("inf")
    max_num = float("-inf")

    for n in numbers:
        # Calculate the sum of the digits
        digit_sum = sum(int(digit) for digit in str(n))

        # Check if the digit sum equals 30
        if digit_sum == 30:
            # Update min and max only when a valid number is found
            min_num = min(min_num, n)
            max_num = max(max_num, n)

    # Calculate the difference if any valid numbers are found
    return max_num - min_num if min_num != float("inf") else 0


# Example usage:
import random

# Generate a list of 1 million random integers between 1 and 100,000
numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Calculate the difference
difference = get_difference(numbers)
print(difference)
