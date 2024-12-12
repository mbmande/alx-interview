#!/usr/bin/python3

"""
-------------------------------
-------------------------
----------------
"""


def isWinner(x, nums):
    """

    000000000000000000000000000000000000
    000000000000000
    """

    if x < 1 or not nums:
        return None
    def sieve(n):
        """
        ------------------------------
        ----------------
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1
        return [num for num, prime in enumerate(is_prime) if prime]

    max_n = max(nums)
    primes = sieve(max_n)

    def play_game(n):
        """
        ====================================
        =============
        """
        primes_set = set(primes)
        primes_in_game = [p for p in primes if p <= n]
        current_player = 0

        while primes_in_game:
            prime = primes_in_game.pop(0)
            primes_set.remove(prime)
            multiples = range(prime, n + 1, prime)
            primes_in_game = [p for p in primes_in_game if p not in multiples]
            current_player = 1 - current_player

        return current_player

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
