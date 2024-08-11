#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result
    in exactly n H characters in the file execute only two
    operations in this file: Copy All and Paste.

    Args:
        n (int): Number to calculate the minimum operations to perform
        on to reach by Copy All and Paste only
    """
    number_of_operations = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            number_of_operations += divisor
            n //= divisor
            divisor -= 1
        divisor += 1

    return number_of_operations
