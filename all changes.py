import math

def get_changes(n):
	a = 0
	b = 0
	x = [''] * n
	y = []
	f = 0
	z = 0
	re = []

	for z in range(n):
		y.append(int(math.pow(n,z)))
	y = [t * n for t in y]
	y.reverse()

	z = 0
	for z in range(y[0]):
		zs = z*n
		f = 0

		for z1 in range(n):
			x[z1] = ((zs-f)/y[z1])%(y[z1])
			f += x[z1] * y[z1]
		re.append(x[:])
		
	return re

print get_changes(3)
 