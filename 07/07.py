s = open('07.in').readlines()
prereqs = {}
for p in s:
	g = p.split(' ')
	if g[1] not in prereqs.keys():
		prereqs[g[1]] = [g[7]]
	else:
		prereqs[g[1]].append(g[7])
good = ""
while len(prereqs):
	dings = []
	for k in prereqs.keys():
		found = 0
		for v in prereqs.values():
			if k in v:
				found = 1
		if not found:
			dings.append(k)
	d = min(dings)
	good += d
	del prereqs[d]
print(good)
print(sorted(good))