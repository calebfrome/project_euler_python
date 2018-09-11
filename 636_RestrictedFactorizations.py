squares = []
cubes = []
quads = []

def compute_squares(n):	
	global squares
	seed = len(squares) + 1
	square = seed ** 2
	while square <= n:
		if n % square == 0:
			squares.append(square)
		seed += 1
		square = seed ** 2

def compute_cubes(n):	
	global cubes
	seed = len(cubes) + 1
	cube = seed ** 3
	while cube <= n:
		if n % cube == 0:
			cubes.append(cube)
		seed += 1
		cube = seed ** 3
		
def compute_quads(n):
	global quads
	seed = len(quads) + 1
	quad = seed ** 4
	while quad <= n:
		if n % quad == 0:
			quads.append(quad)
		seed += 1
		quad = seed ** 4
		
def factorial(n):
	for i in range(2,n):
		n *= i
	return n
		
def F(n):
	compute_quads(n)
	print(quads)
	compute_cubes(n)
	print(cubes)
	compute_squares(n)
	print(squares)
	factors = [0,0,0,0,0,0,0,0,0,0]
	rem = n
	count = 0
	
	for q_i0 in range(len(quads)):
		q_0 = quads[q_i0]
		rem /= q_0
		factors[0] = q_0
		for q_i1 in range(q_i0 + 1, len(quads)):
			q_1 = quads[q_i1]
			if rem % q_1 == 0:
				rem /= q_1
				factors[1] = q_1
				for q_i2 in range(q_i1 + 1, len(quads)):
					q_2 = quads[q_i2]
					if rem % q_2 == 0:
						rem /= q_2
						factors[2] = q_2
						for q_i3 in range(q_i2 + 1, len(quads)):
							q_3 = quads[q_i3]
							if rem % q_3 == 0:
								rem /= q_3
								factors[3] = q_3
								for c_i0 in range(len(cubes)):
									c_0 = cubes[c_i0]
									if rem % c_0 == 0:
										rem /= c_0
										factors[4] = c_0
										for c_i1 in range(c_i0 + 1, len(cubes)):
											c_1 = cubes[c_i1]
											if rem % c_1 == 0:
												rem /= c_1
												factors[5] = c_1
												for c_i2 in range(c_i1 + 1, len(cubes)):
													c_2 = cubes[c_i2]
													if rem % c_2 == 0:
														rem /= c_2
														factors[6] = c_2
														for s_i0 in range(len(squares)):
															s_0 = squares[s_i0]
															if rem % s_0 == 0:
																rem /= s_0
																factors[7] = s_0
																for s_i1 in range(s_i0 + 1, len(squares)):
																	s_1 = squares[s_i1]
																	if rem % s_1 == 0:
																		rem /= s_1
																		factors[8] = s_1
																		factors[9] = rem
																		print(factors)
																		count += 1
																		rem = n / factors[0]
																rem *= s_0
																
														rem += c_2
														
												rem *= c_1
												
										rem *= c_0
										
								rem *= q_3
								
						rem *= q_2
					
				rem *= q_1
	
	return count
	

n = factorial(25)
#n = 286654464
f_n = F(n)
print(f_n)