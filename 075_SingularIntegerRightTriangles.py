import math


def length_primitive(length_list, test_len):
    for list_len in length_list:
        if list_len > test_len:
            break
        if test_len % list_len == 0:
            return False
    return True


length_set = set()
for b in range(2, int(math.sqrt(750000))):
    if b % 100 == 0:
        print('gen lengths', b)
    for a in range(1, b):
        length = 2*b*(a+b)
        # if length_primitive(length_set, length):
        length_set.add(length)

count = 0
for length in range(12, 1500001):
    if length % 100 == 0:
        print('test lengths', length)
    valid = 1 if length in length_set else 0
    for pyth_len in sorted(length_set):
        if pyth_len > length/2:
            break
        if length % pyth_len == 0:
            valid += 1
        if valid > 1:
            break
    if valid == 1:
        count += 1

print(count)
