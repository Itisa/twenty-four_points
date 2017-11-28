import time
import random

class task():
	def __init__(self,x,y,name):
		self.x = x
		self.y = y
		self.name = name

def get_obj():
	ss = range(64)
	tasks = []
	for i in ss:
		x = task(i,i*2,"song")
		tasks.append(x)

	return tasks

def get_string():
	s = 'abcdefghijklmnopqrstuvwxyz'
	ss = [x for x in s]
	return ss[:16]

def get_data():
	xs = range(64)
	ds = random.sample(xs,32)
	ds.sort()
	return ds

def find_number(n,f):
	a = range(0,len(n))
	start = 0
	end = len(n) - 1
	middle = 0

	while 1:

		middle = (start + end) / 2

		if n[middle] == f:
			return middle
		else:
			if start >= end:
				return -1

		if n[middle] > f:
			end = middle - 1
		else:
			start = middle + 1

	if n[start+2] == f:
		return start+2
	else:
		return -1

# ds = range(1,20001)
# ds = get_data()
ds = get_string()
# print get_obj()
# ds = get_obj()

f = 'x'
print 'find:',f
if f in ds:
	print 'index:',ds.index(f)
else:
	print 'index:number is not in the list'
t = time.time()
findex = find_number(ds,f)

print 'cost time:',time.time() - t
print 'result:',findex
print 'answer:',ds[findex]
if ds[findex] == f:
	print 'yes'