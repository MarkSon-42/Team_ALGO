# failed: time over

import sys
my_input = sys.stdin.readline

t = int(my_input())
k = int(my_input())
coins = []

result = [0] * (t + 1)
result[0] = 1

for _ in range(k):
	p, n = map(int, input().split())
	coins.append((p, n))

for p, n in coins:
	for i in range(t, 0, -1):
		for j in range(1, n + 1):
			answer = i - (p * j)
			if answer >= 0:
				result[i] += result[answer]

print(result[t])





# new_study & reminding
	# map()은 이터레이터이다.