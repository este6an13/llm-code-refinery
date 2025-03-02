def get_difference(numbers):
    min_num = float("inf")
    max_num = float("-inf")

    for num in numbers:
        # Calculate the digit sum directly within the loop
        n = num
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10

        if digit_sum == 30:
            # Update min and max without separate conditions for potential speed improvement
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    # If no numbers with a digit sum of 30 were found
    if min_num == float("inf"):
        return 0

    return max_num - min_num


# Example usage (assuming the list is defined as `numbers`):
# numbers = [list of integers]
# result = get_difference(numbers)
