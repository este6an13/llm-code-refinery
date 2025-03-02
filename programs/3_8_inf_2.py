import random


def get_difference(num_list):
    # Initialize with large and small infinity to avoid None checks
    min_num, max_num = float("inf"), float("-inf")
    found = False  # Flag to check if we have found any number meeting the criteria

    for num in num_list:
        n = num
        total = 0

        # Directly compute the digit sum
        while n > 0:
            total += n % 10
            n //= 10

        if total == 30:
            found = True
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

    # If no suitable number was found, return None
    if not found:
        return None

    return max_num - min_num


# Example usage with 1 million random integers between 1 and 100,000
random_numbers = [random.randint(1, 100000) for _ in range(10**6)]

# Call the optimized function with the random number list
difference = get_difference(random_numbers)

print(f"The difference is: {difference}")
