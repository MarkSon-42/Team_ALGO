import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, -1, 1, 1, 0, -1]

idx = []

def bfs(row, col, idx):
    queue = deque([(row, col)])
    visited[row][col] = 1
    check = [(row, col)]
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 1:
                continue
            if grid[x][y] < grid[nx][ny]:  # 봉우리 조건에 안맞을 때 (360도 방향 다 작아야함)
                return 0
            if grid[x][y] == grid[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                check.append((nx, ny))
        idx += check

    return 1


mountain = 0

for i in range(n):
    for j in range(m):
        if (i, j) not in idx:
            visited = [[0] * m for _ in range(n)]
            mountain += bfs(i, j, idx)

print(mountain)