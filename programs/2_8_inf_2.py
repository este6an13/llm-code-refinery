def get_difference(numbers):
    # Initialize variables to track the smallest and largest valid numbers
    min_number = None
    max_number = None

    # Loop through each number in the list
    for number in numbers:
        n = number
        total = 0

        # Calculate the digit sum directly in the loop
        while n > 0:
            total += n % 10
            n //= 10

        # Check if it matches the desired digit sum
        if total == 30:
            if min_number is None:
                min_number = number
                max_number = number
            else:
                if number < min_number:
                    min_number = number
                if number > max_number:
                    max_number = number

    # If no valid numbers are found, return 0
    if min_number is None or max_number is None:
        return 0

    # Return the difference between the largest and smallest found numbers
    return max_number - min_number
