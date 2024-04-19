import heapq
import sys

INF = sys.maxsize

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드를 우선순위 큐에 추가
    dis[start] = 0  # 시작 노드의 거리는 0
    while q:
        d, now = heapq.heappop(q)  # 현재 노드와 거리를 가져옴
        if dis[now] < d:  # 이미 더 짧은 경로가 있다면 무시
            continue
        for v, w in graph[now]:  # 인접 노드들에 대해
            cost = d + w  # 새로운 경로의 거리 계산
            if cost < dis[v]:  # 새로운 경로가 더 짧다면
                dis[v] = cost  # 거리 업데이트
                heapq.heappush(q, (cost, v))  # 우선순위 큐에 추가

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 그래프 초기화
dis = [INF] * (N + 1)  # 거리 배열 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 양방향 그래프
    graph[b].append((a, c))
dijkstra(1)
print(dis[N])


# 근데 겁나 느린거 같은데?