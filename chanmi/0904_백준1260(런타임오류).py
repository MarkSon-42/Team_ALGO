def dfs(graph, current_index, visited, root):
  if not graph:
    return root
  for i in range(len(graph)):
    if (graph[i][0] == current_index and visited[graph[i][1]] != 1):
      current_index = graph[i][1]
      visited[current_index] = 1
      root.append(current_index)
      dfs(graph, current_index, visited, root)
    elif graph[i][1] == current_index and visited[graph[i][0]] != 1:
      current_index = graph[i][0]
      visited[current_index] = 1
      root.append(current_index)
      dfs(graph, current_index, visited, root)
    if len(root) == N:
      return root

def bfs(graph, current_index, visited, root):
  for i in range(len(graph)):
    if graph[i][0] == current_index and visited[graph[i][1]] != 1:
      visited[graph[i][1]] = 1
      root.append(graph[i][1])
    elif graph[i][1] == current_index and visited[graph[i][0]] != 1:
      visited[graph[i][0]] = 1
      root.append(graph[i][0])
    elif len(root) == N:
      return root
  current_index = root[1]
  bfs(graph, current_index, visited, root)  

N = 0
M = 0
V = 0

N, M, V = map(int, input().split())
graph = [0] * (N + 1)
for i in range(M):
  x, y = map(int, input().split())
  graph[i] = [x, y]

print(graph)
visited = [0] * (N + 1)
current_index = V
visited[current_index] = 1
root = [V]
dfs_root = dfs(graph, current_index, visited, root)

visited = [0] * (N + 1)
current_index = V
visited[current_index] = 1
root = [V]
bfs_root = bfs(graph, current_index, visited, root)
print(dfs_root)
print(bfs_root)