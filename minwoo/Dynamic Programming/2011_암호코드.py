n = input()
dp = [0] * (len(n) + 1)

if n[0] == "0":
    print(0)
else:
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(n) + 1):
        if int(n[i - 1]) > 0:
            dp[i] += dp[i - 1]
        if 10 <= int(n[i - 1]) + (10 * int(n[i - 2])) <= 26:
            dp[i] += dp[i - 2]
    print(dp[len(n)] % 1000000)