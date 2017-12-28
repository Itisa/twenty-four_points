import math

def get_changes(n):
	a = 0
	b = 0
	x = range(1,n+1)
	y = []
	for z in range(n):
		y.append(int(math.pow(n,z)))
	y = [t * n for t in y]
	y.reverse()
	# y = [9,3,27]
	print y
	z = 0
	# 1,9,27
	for z in range(95):
		x = [0,0,0]
		for z1 in range(n):
			x[z1] = (z/y[z1])%(y[z1])
		x[-1] = z%(y[-1])-y[0]*x[0]-y[1]*x[1]
		# x[0] = (z/9)%3
		# x[1] = (z/3)%9-3*x[0]	
		# x[2] = z%(27)-3*x[1]-9*x[0]
		print z,':',x
		if x[0] == n-1 and x[1] == n-1 and x[2] == n-1:
			break
		# z += 1
get_changes(4)
 