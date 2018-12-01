x = 0
a = set()
nums = []
with open('01.in','r') as f:
	for line in f:
		l = int(line.strip())
		x += l
		nums.append(l)
print(x)
x = 0
a.add(x)
z = 0
while True:
	for n in nums:
		x += n
		if x in a:
			print(x)
			z = 1
			break
		a.add(x)
	if z == 1:
		break

