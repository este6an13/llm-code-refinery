def get_difference(numbers):
    """Function to find the difference between the smallest and largest numbers
    whose digits sum up to 30."""

    min_number = float("inf")
    max_number = float("-inf")

    for number in numbers:
        digit_sum = 0
        n = number

        while n > 0:
            n, remainder = divmod(n, 10)
            digit_sum += remainder

            # Early termination if the digit sum exceeds 30
            if digit_sum > 30:
                break

        if digit_sum == 30:
            if number < min_number:
                min_number = number
            if number > max_number:
                max_number = number

    # If no numbers met the sum of 30 condition, return 0
    if min_number == float("inf") or max_number == float("-inf"):
        return 0

    return max_number - min_number


# Example usage:
# import random
# random_numbers = [random.randint(1, 100000) for _ in range(1000000)]
# print(get_difference(random_numbers))
