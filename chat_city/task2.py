# 75382602
import sys


def get_input():
	pushes = int(input()) * 2
	vals = {}
	for i in range(4):
		line = tuple(sys.stdin.readline().rstrip())
		for val in line:
			if val == '.':
				continue
			if val not in vals:
				vals[val] = 1
			else:
				vals[val] += 1
	return pushes, vals


def get_score(pushes, vals):
	score = 0
	for k,v in vals.items():
		if pushes >= v:
			score += 1
	return score


data = get_input()
print(get_score(*data))
