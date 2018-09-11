n = 1000000000

while n < 1390000000:
	s = str(n * n)
	if n % 10000000 == 0:
		print(n)
		print(s)
	if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5':
		if s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[18] == '0':
			print(n)
			print(n*n)
			break
	n += 10