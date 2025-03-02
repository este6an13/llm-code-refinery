import csv
import importlib.util
import os
import random
import re
import time

# Constants
NUMBERS_LIST_SIZE = 10**6  # 1 million numbers
RANDOM_MIN = 1
RANDOM_MAX = 100000
CSV_OUTPUT_FILE = "timing_results.csv"
PROGRAMS_FOLDER = "programs"


def _get_difference(numbers):
    def digits_sum(n):
        return sum(int(digit) for digit in str(n))

    smallest = float("inf")
    largest = -float("inf")

    for num in numbers:
        if digits_sum(num) == 30:
            smallest = min(smallest, num)
            largest = max(largest, num)

    return 0 if smallest == float("inf") else largest - smallest


def generate_numbers():
    """Generate a list of 1 million random integers between 1 and 100,000."""
    return [random.randint(RANDOM_MIN, RANDOM_MAX) for _ in range(NUMBERS_LIST_SIZE)]


def find_matching_files():
    """Find all Python files that start with a digit in the programs/ folder."""
    return [f for f in os.listdir(PROGRAMS_FOLDER) if re.match(r"^\d.*\.py$", f)]


def import_get_difference(file_name):
    """Dynamically import get_difference function from a given Python file."""
    module_name = file_name[:-3]  # Remove .py
    file_path = os.path.join(PROGRAMS_FOLDER, file_name)

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, "get_difference"):
        return module.get_difference
    else:
        raise ImportError(f"Module {file_name} does not contain 'get_difference'.")


def measure_execution_time(func, numbers):
    """Measure execution time of a function with the given input."""
    start_time = time.perf_counter()
    result = func(numbers)
    end_time = time.perf_counter()
    return result, end_time - start_time


def parse_filename(file_name):
    """Extract details from filename based on the given structure."""
    match = re.match(r"(\w+)_(\w+)_(\w+)_(\w+)\.py", file_name)
    return match.groups() if match else (None, None, None, None)


def main():
    # Generate two random lists
    numbers_list1 = generate_numbers()
    numbers_list2 = generate_numbers()

    # Compute reference results
    results = [_get_difference(numbers_list1), _get_difference(numbers_list2)]

    # Find matching files
    matching_files = find_matching_files()

    # Prepare CSV file
    with open(CSV_OUTPUT_FILE, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(
            [
                "File Name",
                "Num Agents",
                "Iterations",
                "Time Limit",
                "Replicate",
                "List",
                "Run",
                "Result",
                "Execution Time (s)",
                "Test Passed",
            ]
        )

        for file_name in matching_files:
            try:
                get_difference_func = import_get_difference(file_name)

                for i, numbers in enumerate([numbers_list1, numbers_list2], start=1):
                    for run in range(1, 3):  # Two runs per list
                        result, exec_time = measure_execution_time(
                            get_difference_func, numbers
                        )
                        test_passed = result == results[i - 1]  # Corrected indexing

                        num_agents, iterations, time_limit, replicate = parse_filename(
                            file_name
                        )
                        csv_writer.writerow(
                            [
                                file_name,
                                num_agents,
                                iterations,
                                time_limit,
                                replicate,
                                i,
                                run,
                                result,
                                exec_time,
                                test_passed,
                            ]
                        )

                        status = "PASSED" if test_passed else "FAILED"
                        print(
                            f"Processed {file_name}, List {i}, Run {run}: "
                            f"{exec_time:.4f} seconds, Test: {status}"
                        )

            except Exception as e:
                print(f"Error processing {file_name}: {e}")


if __name__ == "__main__":
    main()
