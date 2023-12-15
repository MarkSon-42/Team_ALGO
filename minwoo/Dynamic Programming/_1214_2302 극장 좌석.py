# https://yabmoons.tistory.com/550

# 참고해서 다시 풀어보기.. ㅠ

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

vips = [int(input()) for _ in range(m)]


dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1

if m > 0:
    pre = 0
    for j in range(m):
        answer *= dp[vips[j] - pre - 1]
        pre = vips[j]
    answer *= dp[n - pre]

else:
    answer = dp[n]

print(answer)