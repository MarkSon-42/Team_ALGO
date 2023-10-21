# 18:00~

import heapq as hq
import sys
my_input = sys.stdin.readline

def dfs(p_adj, cur):
	for i in p_adj[cur]:
		dfs(p_adj, i)
	return cur


n, m = map(int, my_input().split())

adj_h = [[] for _ in range(n+1)]
for i in range(1, m+1):
	r1, r2 = map(int, my_input().split())
	hq.heappush(adj_h[r2], r1)

rst = []
for j in range(1, n+1):
	if len(adj_h[j]) == 0:
		continue
	else:
		for k in adj_h[j]:
			rst.append(dfs(adj_h, k))
		rst.append(j)

print(*rst)
