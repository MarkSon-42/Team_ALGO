from collections import deque
# 성능 면에서 list()보다 deque 형태가 좋다고 함.
# 스택/큐를 구현할 때에는 collections에서 deque 활용해보기

def dfs(v):
    dfs_visited[v] = 1
    print(v, end = ' ')

    for node in graph[v]:
        if not dfs_visited[node]:
            dfs(node)


def bfs(v):
    queue = deque([v])
    bfs_visited[v] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')

        # 앞에서 뺀 node값과 연결된 vertex 찾기
        for j in graph[node]:
            if not bfs_visited[j]:
                bfs_visited[j] = 1
                queue.append(j)

N, M, V = map(int, input().split())

# 간선 그래프 생성 (2차원 배열)
graph = [[] for i in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    # x점과 이어진 노드들의 리스트
    graph[x].append(y)

    # y점과 이어진 노트들의 리스트
    graph[y].append(x)


# dfs와 bfs 모두 용이하도록 정렬
for item in graph:
  item.sort()
# print(graph)

dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)

dfs(V)
print()
bfs(V)