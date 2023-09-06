# BOJ 1260

# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.

# dfs 먼저 구현해보기

N, M, V = map(int, input().split())

g = [[False] * (N + 1) for _ in range(N + 1)]


# 모든 간선에 대해 graph 양방향 초기화
for _ in range(M):
    a, b = map(int, input().split())
    g[a][b] = True
    g[b][a] = True

# 방문노드 초기화

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
def dfs(V):
    visited_dfs[V] = True
    print(V, end = " ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and g[V][i]:
            dfs(i)

def bfs(V):
    pass


dfs(V)
print()
bfs(V)