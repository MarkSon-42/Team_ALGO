# https://magentino.tistory.com/234
# 아.. knapsack의 변형문제였음

import sys
input = sys.stdin.readline



MOD = 10007
n, m, h = map(int, input().split())
blocks_list = [[0] + list(map(int, input().split())) for _ in range(n)]



dp = [[0] * (h + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for h in range(h + 1):
        if dp[i][h]:
            for j in blocks_list[i]:
                if h + j <= h:
                    dp[i + 1][h + j] = (dp[i][h] + dp[i + 1][h + j]) % MOD

print(dp[-1][-1])