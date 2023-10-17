# min heap을 이용한 풀이

import heapq as hq
import sys
my_input = sys.stdin.readline

n = int(my_input())

q = []
for _ in range(n):
	nums = list(map(int, my_input().split()))
	if q:
		for num in nums:
			min_num = q[0]
			if num > min_num:
				hq.heappop(q)
				hq.heappush(q, num)
	else:
		for num in nums:
			hq.heappush(q, num)

print(hq.heappop(q))
