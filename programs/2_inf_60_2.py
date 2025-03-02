def get_difference(numbers):
    # Precompute the digit sums for all numbers from 1 to 99999
    digit_sum_cache = [sum(int(d) for d in str(i)) for i in range(100000)]

    smallest = float("inf")
    largest = -float("inf")
    found = False

    for num in numbers:
        if digit_sum_cache[num] == 30:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
            found = True

    # If found is False, it means no number had digit sum of 30
    return (largest - smallest) if found else 0
