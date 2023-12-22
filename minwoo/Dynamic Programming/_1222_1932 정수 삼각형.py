# dp well-known 문제 중에서도 아주 널리 well-known

#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5

# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 위 조건을 어떻게 처리할 것인지.

# 현재층과 아래층
# 열 인덱스가 자기 자신과 같거나(대각 왼쪽)
# 자기 자신 + 1이거나 (대각 오른쪽)

# 점화식 : dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])


import sys

input = sys.stdin.readline
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

# print(dp)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))


# 후기

# i, j 다 그려보고
# 적어도 예제에 준 만큼은
# 다 max를 구해보면서 규칙성을 찾아야 했다.
