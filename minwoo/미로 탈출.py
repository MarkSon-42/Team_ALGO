from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start, maps, target):
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == -1:
                if maps[nx][ny] == 'X':
                    continue
                if maps[nx][ny] == target:
                    return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1

def solution(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    lever_time = bfs(start, maps, 'L')
    if lever_time == -1:
        return -1
    exit_time = bfs(lever, maps, 'E')
    if exit_time == -1:
        return -1
    return lever_time + exit_time