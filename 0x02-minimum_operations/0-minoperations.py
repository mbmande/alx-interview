#!/usr/bin/python3

"""=====-========-============
"""


def minOperations(n):
    """=-============-==--===
    """
    str = 'H'  # Character to be formed
    operations = 0  # Number of operations needed
    factor = 2  # Starting factor

    if n < 0:
        return 0  # Return 0 if n is negative

    while n > 1:
        while n % factor == 0:
            operations += factor  # Increment operations by factor
            n //= factor  # Divide n by factor

        factor += 1  # Increment factor

    return operations  # Return the total number of operations
