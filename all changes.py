
def get_changes(n):
	a = range(1,n+1)
	b = a[:]
	c = a[:]
	d = 0
	x = []
	for z in b:
		b = c[:]
		for z1 in b:
			
			for z2 in b:
				x.append(z2)
			print x
			b.insert(b[z1-1],b[2])
			b.pop(2)
			x = []
		c.append(c[0])
		c.pop(0)



get_changes(4)
