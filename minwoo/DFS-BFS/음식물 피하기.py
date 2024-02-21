from collections import deque

def bfs(grid, x, y, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    queue = deque([(x, y)])
    visited.add((x, y))
    size = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                size += 1

    return size

def solve():
    N, M, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        grid[r-1][c-1] = 1

    visited = set()
    max_size = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] and (i, j) not in visited:
                max_size = max(max_size, bfs(grid, i, j, visited))

    print(max_size)

solve()