from collections import defaultdict
import re
lines = open('03.in','r').readlines()
stats = []
for line in lines:
	stats.append([int(x) for x in re.findall('\d+',line)])
grid = defaultdict(int)
for stat in stats:
	n, x, y, w, h = stat
	for dx in range(w):
		for dy in range(h):
			grid[(x + dx, y + dy)] += 1
print(len([1 for g in grid.values() if g > 1]))
for stat in stats:
	o = 1
	n, x, y, w, h = stat
	for dx in range(w):
		for dy in range(h):
			if grid[(x + dx, y + dy)] > 1:
				o = 0
	if o:
		print(n)