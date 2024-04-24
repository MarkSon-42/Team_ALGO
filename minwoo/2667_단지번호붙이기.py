import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    if cnt == 0:
        cnt = 1

    answer.append(cnt)

n = int(input())

grid = [list(map(int, input().rstrip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bfs(i, j)

answer.sort()
print(len(answer))

for num in answer:
    print(num)