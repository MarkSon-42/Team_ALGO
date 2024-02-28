import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = 0

    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if grid[nx][ny] == 1:
                    visited[nx][ny] = visited[xx][yy]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[xx][yy] + 1
                    q.append((nx, ny))

    print(visited[n - 1][n - 1])

bfs(0, 0)

