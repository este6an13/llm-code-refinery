def get_difference(numbers):
    smallest = float("inf")
    largest = -float("inf")

    for num in numbers:
        # Optimized sum of digits using arithmetic
        original_num = num
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10

        if digit_sum == 30:
            if original_num < smallest:
                smallest = original_num
            if original_num > largest:
                largest = original_num

    if smallest != float("inf") and largest != -float("inf"):
        return largest - smallest
    else:
        return 0


# Test with an example list 'random_numbers'
# difference = get_difference(random_numbers)
# print("Difference:", difference)
