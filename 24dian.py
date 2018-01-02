import math
from string import maketrans

def x(m,n,o,p):
	x = get_changes()
	e = 0
	while 1:
		e += 1
		if e > 1:
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
		a = 0
		
		for z1 in range(1):
			u = '0123'
			i = '+-*/'
			r = maketrans(u,i)

			fu1 = x[z1][0]
			fu1 = '%d' % fu1
			print fu1
			# fu1.translate(r)

			if fu1 == '+':
				ans1 = a1 + b1

			# if a >= 1 and a <= 16:
			# 	ans1 = a1 + b1
			# 	fu1 = '+'
			# elif a >= 17 and a <= 32:
			# 	ans1 = a1 - b1
			# 	fu1 = '-'
			# elif a >= 33 and a <= 48:
			# 	ans1 = a1 * b1
			# 	fu1 = '*'
			# else:
			# 	ans1 = a1 / b1
			# 	fu1 = '/'
			
			# if a%16 >= 1 and a%16 <=4:
			# 	ans2 = ans1 + c1
			# 	fu2 = '+'
			# elif a%16 >= 5 and a%16 <=8:
			# 	ans2 = ans1 - c1
			# 	fu2 = '-'
			# elif a%16 >= 9 and a%16 <=12:
			# 	ans2 = ans1 * c1
			# 	fu2 = '*'
			# else:
			# 	ans2 = ans1 / c1
			# 	fu2 = '/'

			# if a%4 == 1:
			# 	ans3 = ans2 + d1
			# 	fu3 = '+'
			# elif a%4 == 2:
			# 	ans3 = ans2 - d1
			# 	fu3 = '-'
			# elif a%4 == 3:
			# 	ans3 = ans2 * d1
			# 	fu3 = '*'
			# else:
			# 	ans3 = ans2 / d1
			# 	fu3 = '/'
			
			# if ans3 == 24:
			# 	y = [a1,fu1,b1,fu2,c1,fu3,d1]
			# 	return y
			# return fu1,fu2,fu3

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


print get_changes()
print x(10,10,4,4)