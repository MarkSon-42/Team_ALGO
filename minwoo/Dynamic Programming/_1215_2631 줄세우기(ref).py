# 참고 코드

# https://velog.io/@soobin519/Python-%EB%B0%B1%EC%A4%80-2631-%EC%A4%84%EC%84%B8%EC%9A%B0%EA%B8%B0

# 이걸 못푼건 좀 아깝다. 진짜 골4는 아닌데,...

import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * (n + 1)
children = [0]
for _ in range(n):
    children.append(int(input()))

for i in range(1, n + 1):
    for j in range(1, i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))