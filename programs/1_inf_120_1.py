def get_difference(numbers):
    smallest = float("inf")
    largest = float("-inf")
    found = False

    # Pre-compute possible digits that sum up to 30
    possible_digit_sums = {
        i for i in range(100000) if sum(int(d) for d in str(i)) == 30
    }

    for num in numbers:
        if num in possible_digit_sums:
            found = True
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

    return largest - smallest if found else None


import random

random_numbers = [random.randint(1, 100000) for _ in range(1000000)]
difference = get_difference(random_numbers)
print(difference)
