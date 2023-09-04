from collections import deque
n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# bfs
def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                global cnt
                cnt += 1
                visited[i] = True
                q.append(i)
bfs(1)
print(cnt)