import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
