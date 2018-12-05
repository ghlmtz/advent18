import re
lines = open('04.in','r').readlines()
data = []
for line in lines:
	data.append((re.findall('\d+',line),line))
guards = {}
s = 0
for d in sorted(data):
	time, status = d
	last_num = int(time[-1])
	if "Guard" in status:
		n_guard = last_num
		if n_guard not in guards:
			guards[n_guard] = [0 for _ in range(60)]
	elif "wakes" in status:
		for x in range(s, last_num):
			guards[n_guard][x] += 1
	elif "falls" in status:
		s = last_num
minutesum = [(sum(guards[g]),g) for g in guards]
long_guard = minutesum[minutesum.index(max(minutesum))][1]
print(long_guard * guards[long_guard].index(max(guards[long_guard])))
maxminute = [(max(guards[g]),g) for g in guards]
max_amt, max_guard = max(maxminute)
print(max_guard * guards[max_guard].index(max_amt))