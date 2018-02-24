import random

def get_list(nums):
	ds = nums
	a = 0
	b = -1
	c = []
	x = 0
	y = ds
	for z in range(len(y)):
		x = ds[a]
		b = 0
		for z1 in range(len(ds) - 1):
			b += 1
			if x < ds[b]:
				x = ds[b]
		c.append(x)
		ds.remove(x)
	return c

ds = range(1,100)
xs = random.sample(ds,20)
# xs = [x + 0.1 for x in xs]
print(xs)
ns = get_list(xs)
print(ns)



