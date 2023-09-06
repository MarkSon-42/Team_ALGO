from collections import deque

def bfs(x, y):
  global N, M
  queue = deque()
  queue.append((x, y))
  # 위, 아래 움직임
  dx = [-1, 1, 0, 0]

  # 왼쪽, 오른쪽 움직임
  dy = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    for j in range(4):
        mx = x + dx[j]
        my = y + dy[j]

        if mx > 0 and mx <= N and my > 0 and my <= M:
          if int(maze[mx][my]) == 1:
              queue.append((mx, my))
              maze[mx][my] = int(maze[x][y]) + 1

  return maze[N][M]
   

N, M = map(int, input().split())

maze = [[0] * (M + 1)]

for i in range(N):
    tmp_list = list("0" + input())
    maze.append(tmp_list)

for item in maze:
  print(item)

visited = [([False] * (M + 1)) for i in range(N + 1)]

for item in visited:
   print(item)

print(bfs(1, 1))