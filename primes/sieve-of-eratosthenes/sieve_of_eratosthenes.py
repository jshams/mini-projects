from math import sqrt


def sieve_of_eratosthenes(n):

    primes = [num for num in range(n + 1)]
    # primes[:2] = [False, False]
    primes[0] = primes[1] = False
    for multiple in range(2, int(sqrt(n)) + 1):
        if primes[multiple] is False:
            continue
        for num in range(2*multiple, n+1, multiple):
            primes[num] = False
    return tuple(prime for prime in primes if prime is not False)


if __name__ == '__main__':
    primes_below_100 = sieve_of_eratosthenes(300)
    print(primes_below_100)
