# 428570
import math

min_diff = 1
min_n = None
for d in range(1, 1000000):
    n = math.floor(3/7 * d)
    while n > 0 and d % n == 0:
        n -= 1
    if n == 0:
        continue

    diff = 3/7 - n/d

    if min_diff > diff > 0:
        min_diff = diff
        min_n = n

print(min_n)
