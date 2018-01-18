import math

SCORE = 24

def x(m,n,o,p):
	nums = [m,n,o,p]
	signs = get_changes()
	chas = get_chas()
	ls = len(signs)#256
	lenc = len(chas)#24

	for z in range(lenc):
		a1 = nums[chas[z][0]]
		b1 = nums[chas[z][1]]
		c1 = nums[chas[z][2]]
		d1 = nums[chas[z][3]]		

		for z1 in range(ls):
			fu0 = signs[z1][0]
			fu1 = signs[z1][1]
			fu2 = signs[z1][2]

			ans1 = get_signs(fu0,a1,b1)
			ans2 = get_signs(fu1,ans1,c1)
			ans3 = get_signs(fu2,ans2,d1)
			if ans3 == SCORE:
				return a1,fu0,b1,fu1,c1,fu2,d1

	return 'nothing'
			
def get_signs(s,a,b):
	
	if s == 0:
		ans = a + b
	elif s == 1:
		ans = a - b
	elif s == 2:
		ans = a * b
	else:
		if b != 0:
			if a/b != a/b*b:
				return -100
			ans = a / b
		else:
			return -100

	return ans		

def get_changes():
	x = [''] * 4
	y = [256,64,16,4]
	re = []
	z = 0
	for z in range(256):
		zs = z*4
		f = 0
		for z1 in range(4):
			x[z1] = ((zs-f)/y[z1])%(y[z1])
			f += x[z1] * y[z1]
		re.append(x[1:])
	return re


def get_chas():
	x = [''] * 4
	y = [256,64,16,4]
	re = []
	z = 0
	for z in range(256):
		zs = z*4
		f = 0
		for z1 in range(4):
			x[z1] = ((zs-f)/y[z1])%(y[z1])
			f += x[z1] * y[z1]
		if x.count(1) == 1 and x.count(2) == 1 and x.count(3) == 1:
			re.append(x[:])
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
	for z in range(4):
		c[z*2] = '%d' % c[z*2]
	
	if lis[1] < 2 and lis[3] > 1:
		c.insert(0,'(')
		c.insert(4,')')			
	elif lis[1] < 2 and lis[5] > 1:
		c.insert(0,'(')
		c.insert(6,')')
	elif lis[3] < 2 and lis[5] > 1:
		c.insert(3,'(')
		c.insert(6,')')
	return c

an = x(1,2,3,4)
print ''.join(final(an))
