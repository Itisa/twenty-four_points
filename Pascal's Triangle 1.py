
def get_trianglef(f):
	a = 0
	b = []
	c = [1]
	for z in range(f):
		b = []

		for z1 in range(f - len(c)):
			print '',

		for z1 in range(len(c)):
			print c[z1],
			b.append(c[z1])
		print ''

		a = len(c) - 1
		c = []

		for z1 in range(a):
			c.append(b[z1] + b[z1 + 1])
		c.insert(0,1)
		c.append(1)


get_trianglef(9)