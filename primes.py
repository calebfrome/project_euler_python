import numpy as np
primes = []


def import_primes(max_prime=1000000, max_num_primes=78498):
    prime_file = open('primes.txt')
    while prime_file.readable() and len(primes) < max_num_primes:
        prime = prime_file.readline().rstrip()
        if int(prime) > max_prime:
            break
        primes.append(int(prime))


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def factor(x):
    x_rem = x
    prime_factors = set()
    prime_index = 0
    while x_rem > 1:
        if is_prime(x_rem):
            prime_factors.add(x_rem)
            break
        prime = primes[prime_index]
        if x_rem % prime == 0:
            x_rem /= prime
            prime_factors.add(prime)
        else:
            prime_index += 1
    return list(prime_factors)

