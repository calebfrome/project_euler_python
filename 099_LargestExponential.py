# not 515, 848, 849

def value(line):
	a = line.split(',')
	return a[0] + 4*a[1][:-2]

f = open("099.txt", "r")
lines = f.readlines()

line_num = 0
max_line_num = 0
max = 0

for i in lines:
	val = int(value(i))
	if val > max:
		max = val
		max_line_num = line_num
	
	line_num += 1

print(max_line_num)	