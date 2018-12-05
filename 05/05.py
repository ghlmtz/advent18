import string
s = open('05.in','r').read()
copy = s
ltrs = []
for x,y in zip(string.ascii_lowercase,string.ascii_uppercase):
	ltrs.extend([x+y,y+x])
while True:
	n = len(s)
	for ltr in ltrs:
		s = s.replace(ltr,'')
	if len(s) == n:
		print(len(s))
		break
lens = []
for remove_ltr in string.ascii_lowercase:
	s = copy.replace(remove_ltr,'')
	s = s.replace(remove_ltr.upper(),'')
	while True:
		n = len(s)
		for ltr in ltrs:
			s = s.replace(ltr,'')
		if len(s) == n:
			lens.append(len(s))
			break
print(min(lens))
