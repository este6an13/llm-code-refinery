def get_difference(numbers):
    def digit_sum(n):
        """Compute sum of digits of an integer using arithmetic."""
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total

    min_valid = float("inf")  # Use infinity to simplify the checking process
    max_valid = float("-inf")  # Use negative infinity

    for num in numbers:
        if digit_sum(num) == 30:
            if num < min_valid:
                min_valid = num
            if num > max_valid:
                max_valid = num

    if min_valid == float("inf") or max_valid == float("-inf"):
        # If no numbers were found with the digit sum of 30, return 0.
        return 0

    # Return the difference
    return max_valid - min_valid


# Example usage:
# numbers = [your array of numbers]
# difference = get_difference(numbers)
# print(difference)
