import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visted = [[False] * m for _ in range(n)]

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dfs(r, c):
    global flag
    if r >= n:
        flag = True
    if 0 <= r < n and 0 <= c < m and not visted[r][c] and array[r][c] == 0:
        visted[r][c] = True
        for drc in d:
            dr = r + drc[0]
            dc = c + drc[1]
            dfs(dr, dc)


flag = False
for c in range(m):
    if array[0][c] == 0:
        dfs(0, c)

if flag:
    print('YES')
else:
    print('NO')