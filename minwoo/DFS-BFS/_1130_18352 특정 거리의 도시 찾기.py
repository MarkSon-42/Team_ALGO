# BFS 유형중에서
# 맵 도는 유형 다음으로 잘 등장하는
# 진짜 그래프 탐색 문제
# 노드랑 간선 개념이 주어지는 유형 ㅇㅇ

# bfs - graph type
# cf. bfs - grid(map), ...

import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향  a to b

dist = [-1] * (n + 1)
dist[x] = 0

queue = deque([x])
while queue:
    current = queue.popleft()
    for nxt in graph[current]:
        if dist[nxt] == -1:
            dist[nxt] = dist[current] + 1
            queue.append(nxt)

check = 0  # 최단거리 플래그

for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        check = 1

if check == 0:
    print(-1)