from collections import deque
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	towers = list(map(int, my_input().split()))
	towers = [[t] for t in towers]
	idx = 1
	for t in towers:
		t.append(idx)
		idx += 1
	towers = deque(towers)
	towers.reverse()

	rst = []
	towers_len = len(towers)
	for _ in range(towers_len):
		now, _ = towers.popleft()
		no_town = 1
		for tower in towers:
			if now < tower[0]:
				rst.append(tower[1])
				no_town = 0
				break
		if no_town == 1:
			rst.append(0)

	rst.reverse()
	print(' '.join(map(str, rst)))
