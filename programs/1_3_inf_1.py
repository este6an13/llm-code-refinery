def get_difference(numbers):
    def digits_sum(n):
        return sum(int(digit) for digit in str(n))

    smallest = float("inf")
    largest = -float("inf")

    for num in numbers:
        if digits_sum(num) == 30:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

    if smallest == float("inf") or largest == -float("inf"):
        return 0  # or raise an exception, depending on requirements

    return largest - smallest


# Example usage:
import random

# Generating a list of 1 million random numbers between 1 and 100,000
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Calculate the difference
difference = get_difference(random_numbers)
print(difference)
