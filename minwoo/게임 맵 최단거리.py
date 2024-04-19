from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    if maps[n - 1][m - 1] != 1:
        return maps[n - 1][m - 1]
    else:
        return -1

