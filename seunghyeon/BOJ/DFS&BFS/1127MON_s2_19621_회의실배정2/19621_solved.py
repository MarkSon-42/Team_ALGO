import sys
my_input = sys.stdin.readline

n = int(my_input())
meetings = [list(map(int, my_input().split())) for _ in range(n)]
meetings.sort(key=lambda x: x[0])


dp = [0] * n
dp[0] = meetings[0][2]
for i in range(1, n):
	dp[i] = max(dp[i-1], dp[i-2] + meetings[i][2])

print(dp[n-1])
