def get_difference(numbers):
    """Returns the difference between the largest and smallest numbers
    whose digits sum up to exactly 30."""

    min_num, max_num = float("inf"), float("-inf")

    for number in numbers:
        # Calculate the digit sum using arithmetic, which is already efficient
        digit_sum = sum(int(char) for char in str(number))

        # If the digit sum equals 30, consider the number for min/max update
        if digit_sum == 30:
            if number < min_num:
                min_num = number
            if number > max_num:
                max_num = number

    # If no valid number found, return 0 or handle appropriately
    if min_num == float("inf"):
        return 0

    return max_num - min_num
