# < 답도 맞고 pythonic한 좋은 풀이 >
    # cf) C로 풀 때 인접행렬 만들기 == python으로 풀 때 인접 리스트 만들기 + !!인접리스트[i].sort해주기!!

from collections import deque
import sys
my_input = sys.stdin.readline


def dfs(cur):
    dfs_visited[cur] = True
    print(cur, end=" ")
    for i in graph[cur]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(cur):
    q = deque([cur])
    bfs_visited[cur] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                q.append(i)


if __name__ == "__main__":
    N, M, V = map(int, my_input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, my_input().split())
        graph[x].append(y)
        graph[y].append(x)

    # print(graph)의 결과: [[], [2, 4, 3], [1, 4], [1, 4], [1, 2, 3]]
    for i in graph:
        i.sort()
    # print(graph)의 결과: [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

    dfs_visited = [False] * (N + 1)
    dfs(V)
    print()
    bfs_visited = [False] * (N + 1)
    bfs(V)
