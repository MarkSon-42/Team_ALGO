import heapq as hq
import sys
my_input = sys.stdin.readline

n = int(my_input())

h = []
rst = 0
for _ in range(n):
	hq.heappush(h, int(my_input().strip()))

for i in range(n-1):
	if i == 0:
		rst = hq.heappop(h) + hq.heappop(h)
		hq.heappush(h, rst)
	else:
		tmp = hq.heappop(h) + hq.heappop(h)
		rst += tmp
		hq.heappush(h, tmp)

print(rst)
