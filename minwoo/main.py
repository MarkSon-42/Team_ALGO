from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

# 2-21-12-21-1  dx, dy 에서 방향설정 테크닉
# 상하좌우대각선은?
# 1, 1, 1,  0,  0, -1, -1, -1
# 0, 1, -1, -1, 1, 0, 1, -1

# 0, 0, 1, 1, 1, -1, -1, -1
# 1, -1, 0, 1, -1, 0, 1, -1

# 00111-1-1-1
# 1-101-101-1

def bfs(x, y, e_x, e_y):
    q = deque()
    q.append((x, y))
    matrix[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == e_x and y == end_y:
            return matrix[x][y] - 1  # why decrease 1 ?
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                q.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1

t = int(input())
while t:
    l = int(input())
    matrix = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    if start_x == end_x and start_y == end_y:
        print(0)
        t -= 1
        continue
    answer = bfs(start_x, start_y, end_x, end_y)
    print(answer)
    t -= 1