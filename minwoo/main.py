# 5972 택배배송

n, m = map(int, input().split())

# 헛간 : 정점
# 소들의 길 : 간선
# 소 마리 수 : 가중치 : 거리

# 가중치 그래프에서 bfs구현하기? 가중치 떄문에 힘들다..
# 최단거리 다익스트라 쓰면 됨. ( 최소비용, 최소값 등등.. )


import heapq
import sys

INF = sys.maxsize


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dis = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)
print(dis[N])
