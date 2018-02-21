import math

SCORE = 24

def get_24_point(m,n,o,p):
	nums = [m,n,o,p]
	signs = get_changes()
	chas = get_chas()
	ls = len(signs)#256
	lenc = len(chas)#24
	ans = []

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
				if not [a1,fu0,b1,fu1,c1,fu2,d1] in ans:
					ans.append([a1,fu0,b1,fu1,c1,fu2,d1])


	if ans == []:	
		return ''
	else:

		a = [0,1,2,3]
		b = ['+','-','*','/']

		for z in ans:
			x = ans.index(z)

			
			for z1 in range(4):
				z[z1*2] = '%s' % z[z1*2]
			
			if z[1] < 2 and z[3] > 1:
				z[0] = '(' + z[0] 	
				z[2] = z[2] + ')'
			elif z[1] < 2 or z[3] < 2 and z[5] > 1:
				z[0] = '(' + z[0] 
				z[4] = z[4] + ')'
			elif z[3] < 2 and z[5] > 1:
				z[4] = '(' + z[4] 
				z[6] = z[6] + ')'

			for z1 in range(3):
				z[z1*2+1] = b[a.index(z[z1*2+1])]
			
			ans[x] = z
		anss = []
		fin = ans[:]
		for z in fin:		
			anss.append(''.join(z))
		
		return anss

def get_signs(s,a,b):
	
	if s == 0:
		ans = a + b
	elif s == 1:
		ans = a - b
	elif s == 2:
		ans = a * b
	else:
		if b != 0:
			if a != a/b*b:
				return -1000
			else:
				ans = a / b
		else:
			return -1000

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


if __name__ == '__main__':
	
	fin = get_24_point(1,2,3,6)
	print fin


