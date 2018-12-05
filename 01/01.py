import itertools
x = 0
a = set()
nums = [int(n.strip()) for n in open('01.in','r').readlines()]
print(sum(nums))
for n in itertools.cycle(nums):
	x += n
	if x in a:
		print(x)
		break
	a.add(x)