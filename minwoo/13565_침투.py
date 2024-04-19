from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(m)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == m - 1:
            print('YES')
            exit(0)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx, ny))

for i in range(n):
    if grid[0][i] == 0:
        bfs(0, i)


print("NO")

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:

        if x == m - 1:
            print('YES')
            exit(0)

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1:
                grid[nx][ny] = 1
                q.append((nx, ny))


for i in range(n):
    if grid[0][i] == 0:
        bfs(0, i)

print('NO')



