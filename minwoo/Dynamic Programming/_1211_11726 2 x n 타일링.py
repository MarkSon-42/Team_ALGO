# 음.. c++에 비해서 진짜 엄청나게 느리다.

MAX_N = 1000

n = int(input())
dp = [0] * (MAX_N + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
