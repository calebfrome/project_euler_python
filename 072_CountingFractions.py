# 303963552391 #

import numpy as np
import primes


primes.import_primes()
set_size = 0

for d in range(2, 1000001):
    if d % 10000 == 0:
        print(d)

    factors = primes.factor(d)
    coprimes_per_cycle = 1
    for factor in factors:
        coprimes_per_cycle *= factor - 1
    set_size += d * coprimes_per_cycle / np.prod(factors)

print(set_size)
