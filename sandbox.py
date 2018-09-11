seed = 0
cubes = 0
cube_digits = 1

# generate cube list
while True:
	seed += 1
	cube = seed ** 3
	if len(str(cube)) > cube_digits:
		print(cubes)
		cubes = 0
		cube_digits += 1
	cubes += 1