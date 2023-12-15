# 문제가 너무 야무지네 ICPC 2013 기출임.. ㅇㅇ

# 문제 읽어보면 스티커 떼는 케이스가 지그재그임을 알 수 있는데

# dp
t = int(input())

for _ in range(t) :
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))