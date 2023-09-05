# https://recordofwonseok.tistory.com/380

import sys
from collections import deque
input = sys.stdin.readline

def dfs(curr_node):
    for i in graph[curr_node]:
        if visited[i] == -1:
            visited[i] = visited[curr_node] + 1
            dfs(i)

N = int(input())
target_start, target_end = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for _ in range(int(input())):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[target_start] = 0
dfs(target_start)
print(visited[target_end])