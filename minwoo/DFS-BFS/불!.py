import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'F':  # 불난곳은 큐 앞으로
            visited[i][j] = 1
            q.appendleft((i, j, 'F'))
        elif graph[i][j] == 'J':  # 지훈이는 큐 뒤로
            visited[i][j] = 1
            q.append((i, j, 'J'))

def bfs(q):
    while q:
        pass
ans = bfs(q)
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')