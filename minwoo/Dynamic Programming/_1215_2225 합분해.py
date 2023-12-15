# 합분해

# 20 2

# 21

# 0~20중에서 2개 더해서 20이 되는 경우의 수

# 0 20 .. 20 0 -> 21개

# 6 4

# 84

# 이거,

# n = 1, 2, 3, ...  ㄴㄴ

# k = ???

# dp[n] = 2,

# https://it-garden.tistory.com/341

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * 201 for i in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1_000_000_000

print(dp[k][n])

# print(answer % 1000000000) <- 이러면 메모리초과 날것임.. dp테이블 돌릴떄 값이 너무 커져서? ㅇㅇ