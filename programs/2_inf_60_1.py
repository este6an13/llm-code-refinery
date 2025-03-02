def get_difference(numbers):
    def digit_sum(n):
        """Calculate the sum of digits of n using integer arithmetic."""
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    min_number = max_number = None

    for n in numbers:
        if digit_sum(n) == 30:
            if min_number is None:
                min_number = max_number = n
            else:
                if n < min_number:
                    min_number = n
                elif n > max_number:
                    max_number = n

    if min_number is None:
        return 0

    return max_number - min_number


# Example usage
# numbers = [random integers between 1 and 100,000]
# print(get_difference(numbers))
