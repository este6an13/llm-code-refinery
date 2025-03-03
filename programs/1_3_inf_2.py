def get_difference(numbers):
    def digit_sum(n):
        """Compute the sum of the digits of an integer n."""
        return sum(int(digit) for digit in str(n))

    # Initialize variables to store the min and max values
    min_num = None
    max_num = None

    # Single pass to find min and max numbers with digit sum of 30
    for num in numbers:
        if digit_sum(num) == 30:
            if min_num is None or num < min_num:
                min_num = num
            if max_num is None or num > max_num:
                max_num = num

    # Return None if no valid numbers were found
    if min_num is None:
        return None

    # Return the difference between max and min numbers found
    return max_num - min_num


# Example usage:
# numbers = generate_large_input()  # Suppose this function generates the large list
# difference = get_difference(numbers)
# print(f"Difference: {difference}")
