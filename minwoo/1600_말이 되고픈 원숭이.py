
from collections import deque
import sys
input = sys.stdin.readline
monkey_dx = [0, 1, 0, -1]
monkey_dy = [1, 0, -1, 0]
horse_dx = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(n):
    q = deque()
    q.append((0, 0, n))
    count = [[[0] * (n + 1) for _ in range(w)] for _ in range(h)]
    while q:
        x, y, k = q.popleft()
        if x == h-1 and y == w-1:
            return count[x][y][k]
        if k > 0:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if grid[nx][ny] != 1 and count[nx][ny][k-1] == 0:
                        count[nx][ny][k-1] = count[x][y][k] + 1
                        q.append((nx, ny, k-1))
        for i in range(4):
            nx = x + monkey_dx[i]
            ny = y + monkey_dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] != 1 and count[nx][ny][k] == 0:
                    count[nx][ny][k] = count[x][y][k] + 1
                    q.append((nx, ny, k))
    return -1


k = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
result = bfs(k)
print(result)