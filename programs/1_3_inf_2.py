def digit_sum(n):
    """Function to calculate the sum of digits of a number."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def get_difference(numbers):
    min_val = float("inf")
    max_val = float("-inf")

    for number in numbers:
        if digit_sum(number) == 30:
            if number < min_val:
                min_val = number
            if number > max_val:
                max_val = number
            # If we find both min and max as identical (highly unlikely but theoretically possible),
            # we can choose to break if no further useful computation is possible.
            if min_val < float("inf") and max_val > float("-inf"):
                if min_val == max_val:
                    break

    # If min and max have not been updated, return None
    if min_val == float("inf") or max_val == float("-inf"):
        return None

    return max_val - min_val


# Example usage:
import random

# Generating a list of 1 million integers ranging from 1 to 100,000
numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Using the function
difference = get_difference(numbers)
print(difference)
