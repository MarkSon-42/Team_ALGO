# https://www.acmicpc.net/problem/1697
# 백준 bfs 숨바꼭질 문제랑 95% 같은 문제

from collections import deque

def solution(x, y, n):
    MAX_INT = 10 ** 6
    dist = [-1] * (MAX_INT + 1)
    dist[x] = 0

    q = deque([x])
    while q:
        curr = q.popleft()
        if curr == y:
            return dist[curr]
        for next in (curr + n, curr * 2, curr * 3):
            if 0 <= next <= MAX_INT and dist[next] == -1:
                dist[next] = dist[curr] + 1
                q.append(next)
    return -1