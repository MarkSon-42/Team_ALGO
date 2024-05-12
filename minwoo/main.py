#  1. 전체 배열 순회 ( 시작점 start i, start j )

import sys

sys.stdin = open('input.txt', 'r')

def dfs(n, ci, cj, v):
    global answer
    if n > 3:
        return
    if n == 3 and (si, sj) == (ci, cj):
        answer = max(answer, len(v))
        return

    for k in range(n, n + 2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k, ni, nj, v)
            v.pop()

di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for si in range(N - 2):
        for sj in range(1, N - 1):
            dfs(0, si, sj, [])

    print(f"#{tc} {answer}")