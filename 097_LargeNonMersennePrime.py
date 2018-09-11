n = 28433

for i in range(7830457):
	if i % 100000 == 0:
		print(i)
	n *= 2
	n = int(str(n)[-10:])
	
print(n+1)