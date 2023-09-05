from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))

cnt = 1

distance = [[0 for j in range(m)] for _ in range (n)]
visited = [[False for j in range(m)] for _ in range (n)]

# 시작지점부터 방문하는곳까지의 cnt수를 갱신한다.
def bfs(r, c):
    q = deque([(r, c)])
    while q:
        x, y = q.popleft()
bfs(0, 0)