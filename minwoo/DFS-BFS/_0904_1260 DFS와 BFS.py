from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True  # 양방향을 초기화
    graph[b][a] = True

visited_dfs = [False] * (N + 1)  # dfs 방문기록 초기화
visited_bfs = [False] * (N + 1)  # bfs 방문기록 초기화

def dfs(V):
    visited_dfs[V] = True  # V는 시작노드. 시작 노드를 방문처리
    print(V, end = " ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]:
            dfs(i)



def bfs(V):
    queue = deque([V])
    visited_bfs[V] = True
    while queue:  # queue가 빌 때 까지
        V.queue.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited_bfs[i] and graph[V][i]:
                queue.append(i)
                visited_bfs[i] = True



dfs(V)
print()
bfs(V)

