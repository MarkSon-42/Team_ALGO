# 03:35 ~ 03:50

import sys
my_input = sys.stdin.readline

k, n = map(int, my_input().split())
lines = [int(my_input().rstrip()) for _ in range(k)]

s, e = 0, max(lines)
while s <= e:
	m = (s+e) // 2
	now_cnt = 0
	if m == 0:
		now_cnt = sum(lines)
	else:
		for line in lines:
			if line >= m:
				now_cnt += (line // m)
	if now_cnt < n:
		e = m - 1
	else:
		s = m + 1

print(e)
