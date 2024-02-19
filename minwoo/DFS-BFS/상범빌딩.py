import sys
from collections import deque
input = sys.stdin.readline
dz = (1, -1, 0, 0, 0, 0)
dx = (0, 0, 1, -1, 0, 0)
dy = (0, 0, 0, 0, 1, -1)


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    board = []
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    for _ in range(l):
        board.append([list(input().strip()) for _ in range(r)])
        temp = input()

    q = deque()
    escaped = False

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    start = (i, j, k, 0)
                    visited[i][j][k] = True
                if board[i][j][k] == 'E':
                    goal = (i, j, k)

    q.append(start)
    while q:
        # print(f'cur q: {q}')
        z, x, y, d = q.popleft()
        if (z, x, y) == goal:
            escaped = True
            print(f'Escaped in {d} minute(s).')
            break
        nd = d + 1

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c and not visited[nz][nx][ny]:
                if board[nz][nx][ny] == '.' or board[nz][nx][ny] == 'E':
                    q.append((nz, nx, ny, nd))
                    visited[nz][nx][ny] = True

    if not escaped:
        print('Trapped!')