def get_sum(nums):
	children = nums.pop(0)
	meta = nums.pop(0)
	s = 0
	if children == 0:
		for _ in range(meta):
			s += nums.pop(0)
	else:
		children_sums = dict([(x+1,get_sum(nums)) for x in range(children)])
		for _ in range(meta):
			m = nums.pop(0)
			if m in children_sums:
				s += children_sums[m]
	return s

line = open('08.in').read()
nums = [int(x) for x in line.split(' ')]
print(get_sum(nums))