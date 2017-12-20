import math

def get_changes(n):
	a = 0
	b = 0
	x = range(1,n+1)
	y = []
	for z in x:
		y.append(int(math.pow(n,z)))
	y.reverse()
	print y

	for z in range(20):
		x[0] = z/y[0]
		x[1] = z/y[1]
		x[2] = z/y[2]
		print z,':',x

get_changes(3)
