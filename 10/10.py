import re
lines = open('10.in').readlines()
positions = []
velocities = []
for line in lines:
	p1, p2, v1, v2 = [int(x) for x in re.findall('\-?\d+',line)]
	positions.append([p1,p2])
	velocities.append((v1,v2,))
for i in range(50000):
	for N in range(len(positions)):
		positions[N][0] += velocities[N][0]
		positions[N][1] += velocities[N][1]
	#if(i == 10638):
	#	break
	if(max(positions, key=lambda y:y[1])[1] - min(positions, key=lambda y:y[1])[1]<= 10):
		break
minx = min(positions, key=lambda x:x[0])[0]
miny = min(positions, key=lambda y:y[1])[1]
maxx = max(positions, key=lambda x:x[0])[0]
maxy = max(positions, key=lambda y:y[1])[1]
for N in range(len(positions)):
	positions[N][0] -= minx
	positions[N][1] -= miny
l = [['.' for x in range(70)] for y in range(70)]
for pos in positions:
	x,y = pos
	l[y][x] = '#'
for a in l:
	print(''.join(a))
print(i+1)