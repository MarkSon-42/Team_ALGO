# dp로 점화식 찾기
# 대각 dx는 아닌거 같음..
# dp[i][j] = max(dp[i+1][j+1], dp[i-1][j-1])

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]



