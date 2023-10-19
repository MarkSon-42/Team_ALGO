# failed: time over

import sys
my_input = sys.stdin.readline

n = int(my_input())
lessons = [list(map(int, my_input().split())) for _ in range(n)]
lessons.sort(key=lambda x: x[2], reverse=True)

rooms = []
cnt = 0
for l in lessons:
	if not rooms:
		rooms.append(l)
		cnt += 1
	else:
		change = 0
		for r in rooms:
			if l[2] <= r[1]:
				rooms.insert(rooms.index(r), l)
				rooms.remove(r)
				rooms.sort(key=lambda x: x[1])
				change = 1
				break
		if change == 0:
			rooms.append(l)
			cnt += 1

print(cnt)
