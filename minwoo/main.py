# 문제가 정말 JMT

from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

def bfs(field, cost, n):
    queue = deque([(0, 0)])

    cost[0][0] = field[0][0]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if cost[y][x] + field[ny][nx] < cost[ny][nx]:
                    cost[ny][nx] = cost[y][x] + field[ny][nx]
                    queue.append((nx, ny))

    return cost[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break

    answer += 1

    field = [list(map(int, input().split())) for _ in range(n)]

    cost = [[1e9 for _ in range(n)] for _ in range(n)]

    print(f"Problem {answer}: {bfs(field, cost, n)}")

