from collections import deque

players, topscore = [int(x) for x in open('09.in').read().split() if x.isdigit()]
scores = [0 for _ in range(players)]
marbles = deque([0])
current_player = 0

for marble in range(1,topscore*100+1):
	if marble % 23:
		marbles.rotate()
		marbles.append(marble)
		marbles.rotate()
	else:
		marbles.rotate(-7)
		scores[current_player] += marble + marbles.popleft()
		marbles.rotate()
	current_player = (current_player + 1) % players
	if marble == topscore:
		print(max(scores))
print(max(scores))