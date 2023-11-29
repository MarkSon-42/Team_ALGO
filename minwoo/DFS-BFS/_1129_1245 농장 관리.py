import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, -1, 1, 1, 0, -1]

idx = []

def bfs(x, y, idx):
    queue = deque([(x, y)])

    return 1


mountain = 0

for i in range(n):
    for j in range(n):
        if (i, j) not in idx:
            visited = [[0] * m for _ in range(n)]
            mountain += bfs(i, j, idx)

print(mountain)