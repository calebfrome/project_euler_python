n = 50000

def relPrime(a, b):
	factor = 2
	if a == b:
		return False
	while factor <= b/2:
		if a % factor == 0:
			if b % factor == 0:
				return False
		factor += 1
	return True

def F(num):
	threshold = 10
	sum = 1
	sum_ab = 3
	a = 0
	b = 0
	count = 1
	while(sum <= num):
		if sum_ab % 2 == 0:
			a = sum_ab/2
		else:
			a = (sum_ab-1)/2
		b = sum_ab - a
		while(b < sum_ab):
			if relPrime(a, b):
				#print str(a) + "," + str(b)
				sum += b
				count += 1
				if sum > num:
					return count
				sum += a
				count += 1
				if sum > num:
					return count
			a -= 1
			b += 1
		sum_ab += 1
		if sum > threshold:
			print "sum = " + str(sum)
			threshold *= 10

print "F(" + str(n) + ") is " + str(F(n))