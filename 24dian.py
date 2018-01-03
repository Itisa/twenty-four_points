import math

def x(m,n,o,p):
	m = float(m)
	n = float(n)
	o = float(o)
	p = float(p)
	x = get_changes()
	e = 0

	while 1:
		e += 1
		if e > 24:
			return 'nothing'
			break
		if e == 1:
			z = [m,n,o,p]
		if e == 5:
			z = [m,n,p,o]
		if e == 9:
			z = [n,m,o,p]
		if e == 13:
			z = [n,m,p,o]
		if e == 17:
		 	z = [m,p,n,o]
		if e == 21:
			z = [m,o,n,p]	

		z.append(z[0])
		z.pop(0)
		a1 = z[0]
		b1 = z[1]
		c1 = z[2]
		d1 = z[3]
		
		for z1 in range(64):
			fu0 = x[z1][0]
			fu1 = x[z1][1]
			fu2 = x[z1][2]

			ans1 = get_signs(fu0,a1,b1)
			ans2 = get_signs(fu1,ans1,c1)
			ans3 = get_signs(fu2,ans2,d1)
			if ans3 == 24:
				return a1,fu0,b1,fu1,c1,fu2,d1

			
def get_signs(s,a,b):
	if s == 0:
		ans = a + b
	elif s == 1:
		ans = a - b
	elif s == 2:
		ans = a * b
	else:
		ans = a / b
	return ans

def get_changes():
	x = [''] * 4
	y = [256,64,16,4]
	re = []
	z = 0
	for z in range(y[0]):
		zs = z*4
		f = 0
		for z1 in range(4):
			x[z1] = ((zs-f)/y[z1])%(y[z1])
			f += x[z1] * y[z1]
		re.append(x[1:])
	return re

def final(lis):
	if lis == 'nothing':
		return 'nothing'
	a = [0,1,2,3]
	b = ['+','-','*','/']
	c = []
	for z in lis:
		c.append(z)
	for z in range(3):
		c[z*2+1] = b[a.index(c[z*2+1])]
	return c

an = x(5,1,5,5)
print final(an)
