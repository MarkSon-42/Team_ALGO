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



def solution2(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        nx = set()

        for i in s:
            if i + n <= y:
                nx.add(i + n)
            if i * 2 <= y:
                nx.add(i * 2)
            if i * 3 <= y:
                nx.add(i * 3)

        s = nx
        answer += 1

    return -1


def solution3(x, y, n):
    MAX_INT = 10 ** 6
    dp = [0] + [MAX_INT] * MAX_INT
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] != MAX_INT:
            if i + n <= y:
                dp[i + n] = min(dp[i + n], dp[i] + 1)
            if i * 2 <= y:
                dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            if i * 3 <= y:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return dp[y] if dp[y] != MAX_INT else -1