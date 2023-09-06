# BOJ 1260

# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.

# dfs 먼저 구현해보기

N, M, V = map(int, input().split())

g = [[False] * (N + 1) for _ in range(N + 1)]
print(g)

for _ in range(M):