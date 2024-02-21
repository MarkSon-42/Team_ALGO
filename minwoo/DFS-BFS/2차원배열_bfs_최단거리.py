from collections import deque

def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0)])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and distances[nx][ny] == float('inf'):
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    return distances[-1][-1] if distances[-1][-1] != float('inf') else -1

# example usage
grid = [
  [0, 0, 0, 1],
  [1, 0, 0, 0],
  [0, 0, 0, 0]
]

print(bfs(grid))  # Output: 4