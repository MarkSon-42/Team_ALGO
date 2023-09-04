computer = int(input())
edge = int(input())

graph = [[] for i in range(computer+1)]
visited = [0]*(computer+1)

for i in range(edge):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(edge):
    visited[edge] = 1
    for x in graph[edge]:
        if visited[x] == 0:
            dfs(x)

dfs(1)
print(sum(visited)-1)
