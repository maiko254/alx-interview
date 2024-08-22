#!/usr/bin/python3
"""
A function to calculate the minimum number of coins needed to make a
total value using a given set of coins.
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make a total value
    using a given set of coins.
    """
    if total < 0:
        return -1
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
