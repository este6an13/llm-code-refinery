def get_digit_sum(num):
    """Compute the sum of digits in a number."""
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def get_difference(numbers):
    """Find the difference between the smallest and largest numbers whose digits sum to 30."""
    min_num = float("inf")
    max_num = float("-inf")
    found = False

    for num in numbers:
        if get_digit_sum(num) == 30:
            found = True
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

    if not found:
        return None

    return max_num - min_num


# Example usage
import random

# Generate 1 million random integers between 1 and 100,000.
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Find the difference
difference = get_difference(random_numbers)
print(difference)
