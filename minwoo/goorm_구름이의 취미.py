def solve(N):
    MOD = 1000000007
    N %= MOD
    return (N * (N + 1) // 2 % MOD) ** 2 % MOD

N = int(input())
print(solve(N))