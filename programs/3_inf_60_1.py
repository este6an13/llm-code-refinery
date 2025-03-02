def get_difference(numbers):
    def sum_of_digits(n):
        return sum(map(int, str(n)))

    min_number = None
    max_number = None

    for num in numbers:
        if sum_of_digits(num) == 30:
            if min_number is None or num < min_number:
                min_number = num
            if max_number is None or num > max_number:
                max_number = num

    if min_number is None:
        return 0  # or handle this as an exception

    return max_number - min_number


# Example usage:
# Assuming `numbers` is the list of 1 million random integers
# result = get_difference(numbers)
# print(result)
