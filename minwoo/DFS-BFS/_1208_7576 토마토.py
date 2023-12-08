# 이거 언제 풀은거 같은데?
# 한두달전에 푼거 같고 당시에도 코드 따로 뽑아봐서
# 로직이 어떻게 돌아가는지 확인해봤는데
# 이번에도 똑같이 풀었다.


from collections import deque

m, n = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in grid:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer - 1)