# < 답은 맞지만 C 냄새를 풍기는 별로 안좋은 풀이 >
    # 인접 리스트가 아닌 인접 행렬을 사용함 -> 파이썬에선 인접 리스트를 사용해보도록 하자
    # 인덱스를 0 ~ (n - 1)이 아닌 1 ~ n을 사용 -> 무조건적으로 인덱스를 0부터 사용하자


from collections import deque
import sys
my_input = sys.stdin.readline


def dfs(cur, n):
    dfs_visited[cur] = True
    print(cur, end=" ")
    for i in range(n):
        if i + 1 > n:
            break
        if board[cur][i+1] == 1 and dfs_visited[i+1] == 0:
            dfs(i+1, n)


def bfs(cur, n):
    print(cur, end=" ")
    bfs_visited[cur] = True
    q = deque([cur])

    while q:
        now = q.popleft()
        for i in range(n):
            if i + 1 > n:
                break
            if board[now][i + 1] == 1 and not bfs_visited[i + 1]:
                print(i + 1, end=" ")
                q.append(i + 1)
                bfs_visited[i + 1] = True


if __name__ == "__main__":
    N, M, V = map(int, my_input().split())
    board = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, my_input().split())
        board[x][y] = 1
        board[y][x] = 1
    dfs_visited = [False] * (N + 1)
    dfs(V, N)
    print()
    bfs_visited = [False] * (N + 1)
    bfs(V, N)
