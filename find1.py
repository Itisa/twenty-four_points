import time

def find_number(nums,f):
	i = 0
	if f in nums:
		i = nums.index(f)
	else:
		i = -1

	return i

ds = range(1,10000)
f = 123
t = time.time()
findex = find_number(ds,f)
print 'cost time:',time.time() - t

print findex
