#!/usr/bin/python3
"""
Method that calculates the fewest number of operations needed to result in exactly n H
"""

def minOperations(n):
    """
    Calculates the minimum number of operations required to achieve exactly n H characters.
    
    Args:
        n (int): The target number of H characters.
    
    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    result = 0
    x = 2

    while n > 1:
        while n % x == 0:
            result += x
            n //= x
        x += 1

    return result

