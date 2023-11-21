from collections import deque
import sys
my_input = sys.stdin.readline


def solve(s, t):
    q = deque()
    q.append((0, s, t))  # (시작 시간, 시작 점수, 목표 점수)

    while q:
        cnt, s, t = q.popleft()

        if s == t:
            return cnt

        if (t + 3) >= s * 2:
            if visitee[s * 2] == -1:
                q.append((cnt + 1, s * 2, t + 3))

        if visitee[s + 1] == -1:
            q.append((cnt + 1, s + 1, t))


c = int(my_input())
for _ in range(c):
    s, t = map(int, my_input().split())
    visitee = [-1 for _ in range(100001)]
    print(solve(s, t))
