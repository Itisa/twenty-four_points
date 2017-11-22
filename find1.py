import time

def find_number(nums,f):
	a = nums
	middle = 0
	while len(a) != 2:
		middle = (a[0] + a[len(a) - 1]) / 2
		if f == a[len(a) -1]:
			return a[len(a) - 2]
		if f > a[len(a) - 1] or f < a[0]:
			return 'The nummiddleer is out of range.'
		if middle > f:
			a = range(a[0],middle + 1)
		else:
			a = range(middle,a[len(a) - 1] + 1)
		print a[0],len(a)
	print middle,a 
	return a[0] - 1

ds = range(1,20001)
# ds = [x * 2 for x in ds]
f = 20000
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print findex
