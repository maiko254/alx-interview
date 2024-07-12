#!/usr/bin/python3
"""
Module with function returning the minimum number of operations to copy a
character n times
"""


def minOperations(n):
    """
    Function calculating the minimum number of operations required to perform
    copy and paste on a character resulting in n times the character.

    Parameters:
    n (int): Number of characters after Copy All and Paste operations.

    Returns:
    int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n /= divisor
        divisor += 1

    return ops
