import sys
my_input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n + 1)]
dp[1] = 0
history = [i for i in range(n + 1)]
history[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    history[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        history[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        history[i] = i // 2

print(dp[n])
print(n, end=" ")

back_num = n
while history[back_num] != 0:
    print(history[back_num], end=" ")
    back_num = history[back_num]