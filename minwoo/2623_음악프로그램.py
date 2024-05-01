import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    order = list(map(int, input().split()))[1:]
    for i in range(0, len(order) - 1):
        graph[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)


# 위상정렬 문제

# 문제가 위상정렬로 푸는건지 아닌지를 알아야 하고,

# 위의 구현정도를 완전숙지하고 있어야 함.

# 그래프 주어지고 진행차수 주어질때 큐돌리면서 정렬하기.