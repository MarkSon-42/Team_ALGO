# dfs, bfs 둘다 가능할듯
# 전형적인 dx, dy 문제

# ... 되게 쉬운 문제인줄 알았는데 안풀림

# DFS의 경우 pypy로만통과 시킬 수 있었고,
# BFS는 원래 사용했던
# 자료구조인deque가 아니라 set이라는 자료구조를 사용해야함...
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

grid = [list(input()) for _ in range(r)]  # string이니 굳이 mapping을 해줄 필요가 없다..

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

answer = 1
def bfs(x, y):
    global answer
    queue = deque()
    queue.append([x, y, grid[x][y]])
    while queue:
        x, y, ans = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] not in ans:
                queue.append([nx, ny, ans + grid[nx][ny]])
                answer = max(answer, len(ans) + 1)

bfs(0, 0)
print(answer)

