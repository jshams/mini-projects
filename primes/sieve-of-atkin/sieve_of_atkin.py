from math import sqrt


def sieve_of_atkin(lim):
    sieve = [False] * (lim + 1)

    root_n = sqrt(lim)

    for x in range(1, int(root_n) + 1):
        for y in range(1, int(root_n) + 1):

            # first atkin condition
            n = 4 * x**2 + y**2
            if n <= lim:
                if n % 12 == 1 or n % 12 == 5:
                    # use XOR to flip/negate value
                    sieve[n] ^= True

            # second atkin condition
            n = 3 * x**2 + y**2
            if n < lim and n % 12 == 7:
                sieve[n] ^= True

            # third atkin condition
            if x > y:
                n = 3 * x**2 - y**2
                if n < lim and n % 12 == 11:
                    sieve[n] ^= True

    # iterate over all prime factors
    for x in range(5, int(root_n) + 1):
        if sieve[x] is True:
            # mark all multiples of this prime until lim as false in the sieve
            for y in range(2*x, lim + 1, x):
                sieve[y] = False

    sieve[2] = sieve[3] = True
    return tuple(i for i in range(lim) if sieve[i] is True)


primes_below_100 = sieve_of_atkin(300)
print(primes_below_100)
