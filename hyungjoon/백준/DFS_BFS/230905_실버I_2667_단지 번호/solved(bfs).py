from collections import deque
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

apart = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(r, c):
    q = deque([(r, c)])
    cnt = 1
    visited[r][c] = True
    while q:
        x, y = q.popleft()
        # 0이면 더 볼 필요 없으니 넘김
        if graph[x][y] == 0:
            continue

        # 주변을 살펴서 방문하지않은 1의 집을 찾아간다.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 외 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 0인 곳 제외 (사람이 안사는 곳)
            if graph[nx][ny] == 0:
                continue
            # 사람이 사는 곳이고, 아직 방문하지 않은 곳이면 bfs 실행
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(n):
        # 방문처리가 되지 않은 곳이라면 새롭게 탐색
        if not visited[i][j] and graph[i][j] == 1:
            cnt = bfs(i, j)
            if cnt > 0:
                apart.append(cnt)

# 정렬
apart.sort()
print(len(apart))
for i in apart:
    print(i)