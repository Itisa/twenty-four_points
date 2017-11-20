import time

def find_number(nums,f):
	i = 0
	a = nums
	print a.index(f)
	b = 0
	c = 0
	d = 0
	for z in range(22):
	# while len(a) != 1:
		b = int(len(a) / 2 )
		c = a[0]
		if not c == 1:
			d = 2
		else:
			d = 3
		if a[(b + 2) * d / 2 ] >= f:
			a = range(c,b * 3 / 2 + c)
		else:
			a = range(b + c,len(a) + c)
		print c,len(a)	
	return a[0],a

ds = range(1,10001)
f = 100
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print findex
