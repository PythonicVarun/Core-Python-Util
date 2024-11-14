#  Core Python Utils - Embrace simplicity and efficiency
#  Copyright (c) 2024 - present Varun Agnihotri <https://github.com/PythonicVarun>
#
#  This file is part of Core Python Utils.

import time


def number_otp(length: int = 4) -> str:
    """
    Generates a pseudo-random numerical OTP (One-Time Password) of specified length.

    Args:
        length (int): The length of the OTP to be generated. Defaults to 4.

    Returns:
        str: A string representing the generated OTP.
    """
    return str(time.time()).replace(".", "")[-length:][::-1]


# Example usage:
if __name__ == "__main__":
    otp = number_otp()
    print(f"Randomly generated OTP: {otp}")
