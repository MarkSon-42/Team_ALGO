# 대각선이 포함이라는 것..
# 안전 거리에 대한 정의
# 역시 BFS..로 퍼지면서 1인지 검사하며 최대거리를 갱신하면 될듯??
# 이제 딱 실버 bfs는 바로바로 풀 수 있다..

from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

answer = 0


dist = [[0] * m for _ in range(n)]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while q:
        px, py = q.popleft()

        for i in range(8):
            nx, ny = px + dx[i], py + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[px][py] + 1 if not dist[nx][ny] else min(dist[px][py] + 1, dist[nx][ny])

                    visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            bfs(i, j)


print(max(map(max, dist)))