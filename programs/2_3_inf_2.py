def sum_of_digits(n):
    """Helper function to calculate the sum of digits of a number using a mathematical approach."""
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        if digit_sum > 30:
            return digit_sum
        n //= 10
    return digit_sum


def get_difference(numbers):
    """Function to find the difference between the smallest and largest numbers
    in the list whose digits sum up to 30."""

    smallest = float("inf")
    largest = float("-inf")

    for number in numbers:
        if sum_of_digits(number) == 30:
            if number < smallest:
                smallest = number
            if number > largest:
                largest = number

    return (
        largest - smallest
        if smallest != float("inf") and largest != float("-inf")
        else 0
    )


# Example of how you might use this function
import random

# Generate a list of 1 million random integers between 1 and 100,000
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Call the function
difference = get_difference(random_numbers)
print(difference)
