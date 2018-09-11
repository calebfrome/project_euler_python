# 1617243

import math


def P(streak_level, maxN):
	lcm = 1
	for i in range(2, streak_level + 1):
		lcm = (lcm * i) // math.gcd(lcm, i)
	
	if lcm % (streak_level + 1) == 0:
		return 0
		
	P = 0
	n = lcm
	factor = 1
	while n < maxN:
		if n != 1:
			P += 1
		factor += 1
		if (factor * lcm) % (streak_level + 1) == 0:
			factor += 1
		n = lcm * factor
		
	return P


sum = 0
p_val = 0
for i in range(1,32):
	p_val = P(i, int(math.pow(4,i)))
	sum += p_val
	print(str(i) + " -> " + str(p_val))

print("Sum: " + str(sum))