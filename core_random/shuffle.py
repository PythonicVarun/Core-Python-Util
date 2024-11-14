#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import os
import time

from .number import random_number


def shuffle_list(arr: list) -> list:
    """
    Shuffles a list using a pseudo-random number generator based on the current time and process ID.

    Args:
        arr (list): The list to be shuffled.

    Returns:
        list: A new list with the elements shuffled.
    """
    shuffled_list = arr[:]
    length = len(shuffled_list)
    # Combine time and process ID for the seed
    seed = int(time.time() * 1000) + os.getpid()
    for i in range(length - 1, 0, -1):
        seed = random_number(seed)
        swap_index = seed % (i + 1)
        shuffled_list[i], shuffled_list[swap_index] = (
            shuffled_list[swap_index],
            shuffled_list[i],
        )
    return shuffled_list


# Example usage:
if __name__ == "__main__":
    original_list = list(range(15))
    shuffled_list = shuffle_list(original_list)
    print(f"Original List: {original_list}")
    print(f"Shuffled List: {shuffled_list}")
