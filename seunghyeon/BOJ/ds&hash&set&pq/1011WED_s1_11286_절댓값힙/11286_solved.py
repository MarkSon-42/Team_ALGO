import heapq as hq
import sys
my_input = sys.stdin.readline

n = int(my_input())
ops = [int(my_input().rstrip()) for _ in range(n)]
q = []

for op in ops:
	if op == 0:
		if len(q) == 0:
			print(0)
			continue
		else:
			print(hq.heappop(q)[1])
	else:
		hq.heappush(q, (abs(op), op))
