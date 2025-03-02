def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def precompute_digit_sums(limit):
    sums = [0] * (limit + 1)
    for i in range(limit + 1):
        sums[i] = digit_sum(i)
    return sums


def get_difference(numbers):
    min_number = None
    max_number = None

    # Precompute the digit sums for numbers up to 999,999
    precomputed_sums = precompute_digit_sums(999999)

    for number in numbers:
        # Choose computation method based on number size
        if number <= 999999:
            ds = precomputed_sums[number]
        else:
            if number < 270:  # A number below 270 can't sum its digits to 30
                continue
            ds = digit_sum(number)

        if ds == 30:
            if min_number is None or number < min_number:
                min_number = number
            if max_number is None or number > max_number:
                max_number = number

            # Early exit if the minimal realistic bounds are found
            if min_number == 100000 and max_number >= 999999999:
                break

    if min_number is None or max_number is None:
        return 0

    return max_number - min_number


# Example usage:
import random

numbers = [random.randint(1, 1000000000) for _ in range(1000000)]
print(get_difference(numbers))
