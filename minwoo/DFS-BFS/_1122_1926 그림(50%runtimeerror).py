# dx, dy 테크닉
# 그리고 bfs를 쓰는
# 매우 전형적인 원조격에 가까운 문제
# 최근에도 카피문제가 계속 출제됨


from collections import deque


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return 0

n,m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx,dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]

answer = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 1
            graph[i][j] = 0
            bfs(i, j)
            answer.append(cnt)
answer.sort(reverse=True)
print(len(answer))
print(answer[0])

# 아니 이거 왜 50% 에서 런타임 에러 뜨는데..