def get_difference(numbers):
    # Use high initial value for min_number and low initial value for max_number
    # to avoid None checks
    min_number = float("inf")
    max_number = float("-inf")
    found = False

    for num in numbers:
        # Calculate the digit sum once per number
        digit_sum = sum(map(int, str(num)))

        if digit_sum == 30:
            found = True
            # Directly update minimum and maximum without None checks
            if num < min_number:
                min_number = num
            if num > max_number:
                max_number = num

    # If no number with digit sum of 30 was found, return 0
    if not found:
        return 0

    # Return the difference
    return max_number - min_number


# Example usage setup (uncomment to test):
# import random
# numbers = [random.randint(1, 100000) for _ in range(1000000)]
# print(get_difference(numbers))
