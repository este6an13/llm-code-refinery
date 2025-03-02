def get_difference(numbers):
    min_valid_number = float("inf")
    max_valid_number = float("-inf")
    inf = float("inf")

    for number in numbers:
        digit_sum = 0
        n = number

        # Calculate the sum of digits directly with optimizations
        while n > 0:
            digit_sum += n % 10
            n //= 10
            # Break early if the digit sum exceeds 30
            if digit_sum > 30:
                break

        # Update min and max if digit sum is exactly 30
        if digit_sum == 30:
            if number < min_valid_number:
                min_valid_number = number
            if number > max_valid_number:
                max_valid_number = number

    # Return appropriate result if no valid number is found
    if min_valid_number == inf:
        return 0

    return max_valid_number - min_valid_number


# Example usage:
# import random
# random_integers = [random.randint(1, 100000) for _ in range(1000000)]
# print(get_difference(random_integers))
