t = int(input())

# 도형이 생겨먹은것 부터가 dp
# dp[n] = dp[n - 1] + dp[n - 2] 이런 식으로 점화식을 세워야 할텐데 값이 조금 다를 듯

p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
for _ in range(t):
    n = int(input())
    for i in range(4, n + 1):
        p[i] = p[i - 2] + p[i - 3]
    print(p[n])

# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 49 65 86 114 151



# 옛날에 푼 코드

p = [0 for i in range(101)]

p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 101):
    p[i] = p[i - 2] + p[i - 3]

t = int(input())
for i in range(t):
    n = int(input())
    print(p[n])
