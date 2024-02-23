# 핵심은 입력값이 0에서 1로 갔을 때만 체크를 해줘야 한다. 그래야 가장자리 부분만 녹아서 사라지기 때문

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if grid[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    grid[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1

    answer.append(cnt)
    return cnt

t = 0
while True:
    t += 1

    visited = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(t - 1)
print(answer[-2])
