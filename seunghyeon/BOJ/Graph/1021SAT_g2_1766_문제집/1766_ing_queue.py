# 다시 풀어보기!

import heapq as hq
import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
graph = [[] for _ in range(n+1)]
edges = [0] * (n+1)
for i in range(m):
	n1, n2 = map(int, my_input().split())
	graph[n1].append(n2)
	edges[n2] += 1

pq = []
rst = []
for edge in range(1, n + 1):
	if edges[edge] == 0:
		hq.heappush(pq, edge)
while pq:
	node = hq.heappop(pq)
	rst.append(node)
	for i in graph[node]:
		edges[i] -= 1
		if edges[i] == 0:
			hq.heappush(pq, i)

print(*rst)
