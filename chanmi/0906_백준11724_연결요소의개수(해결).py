import sys

# N이 1000인 경우 M이 499500이라는 최악의 숫자가 나올 수 있어서
# 재귀 깊이를 설정해주고 readline을 쓰는 게 속도 줄여줌
sys.setrecursionlimit(10**6)
se = sys.stdin.readline

def dfs(vertex):
  visited[vertex] = True
  for node in graph[vertex]:
    if not visited[node]:
      dfs(node)


N, M = map(int, se().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
  x, y = map(int, se().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [False] * (N + 1)

count = 0
for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)