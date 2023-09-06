from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  
  # 위, 아래 움직임
  dx = [-1, 1, 0, 0]

  # 왼쪽, 오른쪽 움직임
  dy = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    for j in range(4):
        mx = x + dx[j]
        my = y + dy[j]

        if mx >= 0 and mx < N and my >= 0 and my < M:
          if int(visited[mx][my]) == False and graph[mx][my] == 1:
              queue.append((mx, my))
              visited[mx][my] = True

   

T = int(input())
result = []
for t in range(T):
  M, N, K = map(int, input().split())
  graph = [([0] * M) for _ in range(N)]
  worm = 0

  for i in range(K):
    y, x = map(int, input().split())
    graph[x][y] = 1

  # for i in graph:
  #   print(i)

  visited = [([False] * M) for _ in range(N)]

  for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j] == 1:
          bfs(i, j)
          worm += 1
  result.append(worm)

for number in result:
   print(number)