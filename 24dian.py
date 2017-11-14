def x(m,n,o,p):
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
		a = 0
		
		for z1 in range(64):
			a += 1

			if a >= 1 and a <= 16:
				ans1 = a1 + b1
				fu1 = '+'
			elif a >= 17 and a <= 32:
				ans1 = a1 - b1
				fu1 = '-'
			elif a >= 33 and a <= 48:
				ans1 = a1 * b1
				fu1 = '*'
			else:
				ans1 = a1 / b1
				fu1 = '/'
			
			if a%16 >= 1 and a%16 <=4:
				ans2 = ans1 + c1
				fu2 = '+'
			elif a%16 >= 5 and a%16 <=8:
				ans2 = ans1 - c1
				fu2 = '-'
			elif a%16 >= 9 and a%16 <=12:
				ans2 = ans1 * c1
				fu2 = '*'
			else:
				ans2 = ans1 / c1
				fu2 = '/'

			if a%4 == 1:
				ans3 = ans2 + d1
				fu3 = '+'
			elif a%4 == 2:
				ans3 = ans2 - d1
				fu3 = '-'
			elif a%4 == 3:
				ans3 = ans2 * d1
				fu3 = '*'
			else:
				ans3 = ans2 / d1
				fu3 = '/'
			
			if ans3 == 24:
				y = [a1,fu1,b1,fu2,c1,fu3,d1]
				return (y)


print x(6,7,8,9)
#a1 = a
#b1 = b
#c1 = c
#d1 = d