import time
import random

def get_data():
	xs = range(59)
	ds = random.sample(xs,20)
	ds.sort()
	return ds

def find_number(nums,f):
	b = nums
	a = range(0,len(b))
	middle = 0

	while len(a) != 1:	
	# for z in range(10):
		# print a,

		middle = len(a) / 2
		# print middle

		if b[a[middle]] == f:
			return a[middle]
		if b[middle + a[0]] > f:
			a = range(a[0],a[middle])
		else:
			a = range(a[middle],a[-1] + 1)

	if b[a[0]] == f:
		return a[0]
	else:
		return -1

# ds = range(1,20001)
ds = get_data()
# ds = [x * 2 for x in ds]
f = ds[len(ds) / 3]
f = ds[-3] + 1
print 'find ',f
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print ds

print 'result:',findex
print 'answer:',ds[findex]
if ds[findex] == f:
	print 'yes'
# print ds[findex],f
