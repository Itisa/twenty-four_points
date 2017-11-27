import time
import random

def get_data():
	xs = range(500)
	ds = random.sample(xs,251)
	ds.sort()
	return ds

def find_number(nums,f):
	b = nums
	a = range(0,len(b))
	c = 0
	d = 1
	middle = 0

	while (d - c) != 0:
	# for z in range(30):
		# print a,

		middle = (c + d) / 2
		# print middle,

		if b[a[middle]] == f:
			return a[middle]
		if b[middle + a[0]] > f:
			c = a[0 + c]
			d = a[middle - 1 - c]
		else:
			c = a[middle + c]
			d = a[a[-1] / 2]
		# print range(c,d + 1)
		# print c,d

	print b[c+2]
	if b[c+2] == f:
		return c+2
	else:
		return -1

# ds = range(1,20001)
ds = get_data()
# ds = [x * 2 for x in ds]
f = ds[len(ds) / 5]
# f = ds[0]
print 'find:',f
print 'index:',ds.index(f)
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print ds

print 'result:',findex
print 'answer:',ds[findex]
if ds[findex] == f:
	print 'yes'
# print ds[findex],f
