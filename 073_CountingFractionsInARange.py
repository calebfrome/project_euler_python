# 7295372 #
import math

count = 0
for d in range(4, 12001):
    for n in range(math.ceil(d/3), math.floor(d/2)+1):
        if math.gcd(n, d) == 1:
            count += 1

print(count)
