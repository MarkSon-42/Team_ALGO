import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited= [False] * (n+1)
cnt = 0


for i in range(1, n + 1):
    if not visited[i]:  
        if not graph[i]:  
            cnt += 1  
            visited[i] = True  
        else:  
            dfs(i)  
            cnt += 1 

print(cnt)
    
    