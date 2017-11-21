import time

def find_number(nums,f):
	i = 0
	a = nums
	# print a.index(f)
	b = 0
	for z in range(19):
	# while len(a) != 1:
		b = (a[0] + a[len(a) - 1]) / 2
		# if b == f:
		# 	return a[0] + 1
		if b > f:
			a = range(a[0],b + 1)
		else:
			a = range(b,a[len(a) - 1] + 1)
			# d *= 2
		print a[0],len(a)
	print b,a 
	return a[0] - 1

ds = range(1,20001)
# ds = [x * 2 for x in ds]
f = 20000
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print findex
