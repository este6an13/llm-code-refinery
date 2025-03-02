def get_difference(numbers):
    min_num = None
    max_num = None

    for num in numbers:
        total, n = 0, num
        while n > 0:
            total += n % 10
            n //= 10

        if total == 30:
            if min_num is None or num < min_num:
                min_num = num
            if max_num is None or num > max_num:
                max_num = num

    # If no number met the condition, return 0
    if min_num is None:
        return 0

    return max_num - min_num


# Example usage:
# Assuming `random_numbers` is your list of 1,000,000 integers
# result = get_difference(random_numbers)
