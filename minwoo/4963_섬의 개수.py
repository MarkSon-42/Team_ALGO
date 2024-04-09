from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, -1, 1, 0, 0, -1, 1]
dy = [1, 1, -1, -1, 1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny))



while True:
    cnt = 0
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    if w == 0 and h == 0:
        break

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)