#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import os
import time


def random_seed() -> int:
    """
    Generates a random seed based on the current time and process ID.

    Returns:
        int: A pseudo-random seed.
    """
    return int(time.time() * 1000) + os.getpid()


# Example usage:
if __name__ == "__main__":
    seed = random_seed()
    print(f"Random Seed: {seed}")
