def get_difference(numbers):
    def digit_sum(n):
        return sum(int(digit) for digit in str(n))

    min_value = float("inf")
    max_value = float("-inf")
    found = False

    for number in numbers:
        if digit_sum(number) == 30:
            found = True
            min_value = min(min_value, number)
            max_value = max(max_value, number)
            if max_value - min_value >= 99999:  # Optimization: Early exit
                break

    return max_value - min_value if found else 0


# Example usage:
import random

# Generate 1 million random integers between 1 and 100,000
random_numbers = [random.randint(1, 100000) for _ in range(1000000)]

# Call the function and measure the time taken
import time

start_time = time.time()
difference = get_difference(random_numbers)
end_time = time.time()

print("Difference:", difference)
print("Execution Time:", end_time - start_time)
