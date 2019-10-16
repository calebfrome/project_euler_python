# 402 #
import math
link_table = dict()


def next_link(x):
    if link_table.__contains__(x):
        return link_table[x]
    link = 0
    for d in str(x):
        link += math.factorial(int(d))
    link_table[x] = link
    return link


count = 0

for n in range(1000001):
    chain = []
    while n not in chain and chain.__len__() <= 60:
        chain.append(n)
        n = next_link(n)
    if chain.__len__() == 60:
        count += 1

print(count)
