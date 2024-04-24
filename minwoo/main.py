n = int(input())

# dp table : n의 크기에 따라 연산을 하는 횟수의 최솟값을 담는 배열

dp = [0] * 100000005

# x가 3으로 나누어 떨어지면, 3으로 나눈다.
#  ~    2  ~
# 1을 뺀다.




for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])