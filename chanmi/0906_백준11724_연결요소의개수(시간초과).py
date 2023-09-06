import sys
sys.setrecursionlimit(10**6)

def dfs(vertex):
  visited[vertex] = True
  for node in graph[vertex]:
    if not visited[node]:
      dfs(node)


   

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (N + 1)

count = 0
for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)