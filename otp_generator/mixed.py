#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

from string import ascii_letters, digits

from core_random.shuffle import shuffle_list


def mixed_otp(length: int = 5) -> str:
    """
    Generates a mixed alphanumeric OTP (One-Time Password) of a specified length.

    Args:
        length (int): The length of the OTP to generate. Default is 5.

    Returns:
        str: The generated OTP.
    """
    chars = [char for char in ascii_letters] + [num for num in digits]

    overflow = (length // len(chars)) + 1
    if overflow == 1:
        shuffled_list = shuffle_list(chars)
        return "".join(shuffled_list[:length])
    else:
        shuffled_list = shuffle_list(chars * overflow)
        return "".join(shuffled_list[:length])


# Example usage:
if __name__ == "__main__":
    length = 5
    otp = mixed_otp(length)
    print(f"Mixed OTP: {otp}")
