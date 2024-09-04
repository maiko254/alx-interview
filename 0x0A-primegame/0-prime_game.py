#!/usr/bin/python3
"""
This module defines a function to determine the winner of a prime number game.
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the upper limit of the
                     set for each round.

    Returns:
        str: The name of the player who wins the game, or None if the winner
             cannot be determined.
    """
    def is_prime(n):
        """
        Checks if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def play_round(n):
        """
        Plays a round of the prime number game.

        Args:
            n (int): The upper limit of the set for the round.

        Returns:
            bool: True if Maria wins the round, False if Ben wins the round.
        """
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
