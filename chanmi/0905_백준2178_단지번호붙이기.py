from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  count = 1
  visited[x][y] = True
  
  max_result = -10
  # 위, 아래 움직임
  dx = [-1, 1, 0, 0]

  # 왼쪽, 오른쪽 움직임
  dy = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    for j in range(4):
        mx = x + dx[j]
        my = y + dy[j]

        if mx >= 0 and mx < N and my >= 0 and my < N:
          if int(visited[mx][my]) == False and graph[mx][my] == 1:
              queue.append((mx, my))
              visited[mx][my] = True
              count += 1

  return count
   

N = int(input())
graph = []
result = []
for i in range(N):
   graph.append(list(map(int, input())))

visited = [([False] * N) for i in range(N)]
for i in range(N):
   for j in range(N):
      if visited[i][j] == False and graph[i][j] == 1:
         count = bfs(i, j)
         if count > 0:
            result.append(count)

result.sort()
print(len(result))
for i in range(len(result)):
   print(result[i])
