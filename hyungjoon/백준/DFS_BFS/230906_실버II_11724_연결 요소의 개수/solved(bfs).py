'''
문제 : 연결요소의 개수
링크 : https://www.acmicpc.net/problem/11724
소요시간 : 15분
'''
import sys
from collections import deque
se = sys.stdin.readline

n, m = map(int, se().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, se().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결 요소 = 연결되어있는 집합

# n번 노드에 방문했는지 체크하기 위한 visited
visited = [False] * (n+1)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

cnt = 0
# n번 노드를 방문해서 집합이 총 몇개인지 알아낸다.
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)