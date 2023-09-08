# 정말 문제가 거의 똑같다. 바이러스 문제에서 방향만 다른?

from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]  #  idx 맞추기 위해서 N + 1 개 생성

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 단방향 그래프이기 때문에 양방향 초기화 할 필요 없음.

distance = [0] * (N + 1)
distyance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for nd in graph[now]:
        if distance[nd] == 0:
            distance[nd] = distance[now] + 1
            q.append(nd)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)