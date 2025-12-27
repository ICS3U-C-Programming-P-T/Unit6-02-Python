#!/usr/bin/env python3
# Created by: Patrick Tumbaga
# Created on: 12/26/2025
# This program generates random numbers and finds the maximum value

import random

# sets constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


# Find and returns the maximum value in a list using a loop.
def find_max_value(list_of_int):

    max_value = list_of_int[0]

    for index in range(1, len(list_of_int)):
        if list_of_int[index] > max_value:
            max_value = list_of_int[index]

    return max_value


def main():
    numbers = []

    # Generate random numbers
    for _ in range(MAX_ARRAY_SIZE):
        random_number = random.randint(MIN_NUM, MAX_NUM)
        numbers.append(random_number)

    # Display numbers
    print(numbers)

    # Find and display max value
    max_value = find_max_value(numbers)
    print("\n Highest Value Is:", max_value)


if __name__ == "__main__":
    main()
