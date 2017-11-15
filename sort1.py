import random

def get_list(nums):
	ds = nums
	a = -1
	b = 0
	c = []
	d = []
	# for z in range(len(ds) - 1):
	y = len(ds) - 1
	while len(c) != y:
		a += 1
		b = 0
		x = 0
		for z1 in range(len(ds)):
			if ds[a] > ds[b]:
				x += 1
				if x == len(ds) - 1:
					c.append(ds[a])
					ds.remove(ds[a])
					# print a,b,x,
					a = -1
					break
			b += 1
		
	c.append(ds[0])
	return c

ds = range(1,100)
xs = random.sample(ds,20)
# xs = [x + 0.1 for x in xs]
print xs
ns = get_list(xs)
print ns



