# 부분증가수열 dp

# 11053과 유사한 문제?

 
n = int(input())
dp = [(0, 0)] * (n + 1)
answer = 0

for i in range(1, n + 1):
    num = int(input())
    for j in range(i):
        if dp[j][0] < num:
            dp[i] = (num, max(dp[j][1] + 1, dp[i][1]))
            answer = max(answer, dp[i][1])

print(n - answer)