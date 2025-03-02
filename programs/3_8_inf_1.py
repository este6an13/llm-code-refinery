def get_digit_sum(n):
    """Calculate the sum of digits of a number."""
    s = 0
    while n > 0:
        s, n = s + n % 10, n // 10
    return s


def get_difference(numbers):
    target_digit_sum = 30
    min_number = None
    max_number = None

    for number in numbers:
        # Calculate digit sum without casting to string
        digit_sum = get_digit_sum(number)

        if digit_sum == target_digit_sum:
            if min_number is None or number < min_number:
                min_number = number
            if max_number is None or number > max_number:
                max_number = number

    # Calculate the difference only if valid min and max numbers are found
    if min_number is not None and max_number is not None:
        return max_number - min_number
    else:
        return 0


# Example usage:
# numbers_list = ... (a list of 1 million numbers)
# print(get_difference(numbers_list))
