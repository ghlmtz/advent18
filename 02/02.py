lines = open('02.in','r').readlines()
twos = 0
threes = 0
for l in lines:
	c = [l.count(n) for n in l]
	if 2 in c:
		twos += 1
	if 3 in c:
		threes += 1
print(twos * threes)

for N in range(len(lines)):
	for M in range(N):
		s = -1
		for i, (m,n) in enumerate(zip(lines[M],lines[N])):
			if m != n:
				if s != -1:
					s = -2
					break
				else:
					s = i
		if s >= 0:
			print(lines[N][:s] + lines[N][s+1:])