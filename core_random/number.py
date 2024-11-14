#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

from .seed import random_seed


def random_number(seed: int) -> int:
    """
    A simple pseudo-random number generator (PRNG) using a linear congruential generator (LCG) algorithm.

    Args:
        seed (int): The seed value for the PRNG.

    Returns:
        int: The next pseudo-random number.
    """
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = (a * seed + c) % m
    return seed


# Example usage:
if __name__ == "__main__":
    seed = random_seed()
    number = random_number(seed)
    print(f"Random Number: {number}")
