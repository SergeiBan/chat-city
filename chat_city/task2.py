# 75523875
import sys


def get_score(pushes, game_field):
	"""
	Принимает строку  с числом нажатий игрока и список строк, представляющий
	игровую карту. Возвращает число очков, полученных на данной карте.
	"""
	pushes = int(pushes) * 2
	vals = {}
	for line in game_field:
		for val in line:
			if val == '.':
				continue
			if val not in vals:
				vals[val] = 1
			else:
				vals[val] += 1
	score = 0
	for k, v in vals.items():
		if pushes >= v:
			score += 1
	return score


if __name__ == '__main__':
	pushes = input()
	game_field = []
	for i in range(4):
		game_field.append(sys.stdin.readline().rstrip())
	result = get_score(pushes, game_field)
	print(result)
