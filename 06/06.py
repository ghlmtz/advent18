from collections import defaultdict

def mandist(here, there):
	return abs(here[0] - there[0]) + abs(here[1] - there[1])
lines = open('06.in','r').readlines()
nums = []
for line in lines:
	x,y = line.rstrip().split(',')
	nums.append((int(x),int(y)))
minx = min([x for x,y in nums])
maxx = max([x for x,y in nums])
miny = min([y for x,y in nums])
maxy = max([y for x,y in nums])
areas = [0 for x in range(len(nums))]
grid = {}
for x in range(minx,maxx+1):
	for y in range(miny,maxy+1):
		if (x,y) in nums:
			grid[(x,y)] = (nums.index((x,y))+1,0)
			areas[idx] += 1
		else:
			minimum = 10000
			idx = -2
			doublemin = -1
			for n in nums:
				d = mandist((x,y),n)
				if d < minimum:
					minimum = d
					doublemin = 0
					idx = nums.index(n)
				elif d == minimum:
					doublemin = 1
			if doublemin == 0:
				grid[(x,y)] = (idx+1,mandist((x,y),n))
				areas[idx] += 1
				if x == minx or x == maxx or y == miny or y == maxy:
					areas[idx] += float("inf")
			else:
				grid[(x,y)] = (0,0)
print(max([x for x in areas if x != float("inf")]))
inregion = 0
for x in range(minx-200,maxx+200):
	for y in range(miny-200,maxy+200):
		if sum([mandist(n,(x,y)) for n in nums]) < 10000:
			inregion += 1
print(inregion)