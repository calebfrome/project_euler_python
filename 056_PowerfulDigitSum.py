a = 99
b = 99
sum = 0
best_sum = 0

print(a ** b)

for a in range(1,100):
	for b in range(1,100):
		n = a ** b
		s = str(n)
		sum = 0
		for i in range(len(s)):
			sum += int(s[i])
		if sum > best_sum:
			best_sum = sum
			print(best_sum)
			
print(best_sum)
