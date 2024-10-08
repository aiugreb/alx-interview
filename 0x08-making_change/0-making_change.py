#!/usr/bin/python3

""" Change making module"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
