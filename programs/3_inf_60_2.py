def get_difference(numbers):
    min_number = float("inf")
    max_number = -float("inf")
    found = False  # Flag to check if we found any number with digit sum 30

    for num in numbers:
        # Calculate digit sum using integer arithmetic
        digit_sum = 0
        temp = num
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10

        # If the sum of digits is 30, update min and max variables
        if digit_sum == 30:
            found = True
            if num < min_number:
                min_number = num
            if num > max_number:
                max_number = num

    # Return the difference, else None if no valid number was found
    return (max_number - min_number) if found else None


# Example usage:
# result = get_difference(your_list_of_1_million_random_integers)
