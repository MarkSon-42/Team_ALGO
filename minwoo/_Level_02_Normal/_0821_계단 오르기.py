# https://bio-info.tistory.com/158
# BOJ 2579 silver 3

n = int(input())
stair = [int(input()) for _ in range(n)]  # 계단 input

# -> [10, 20, 15, 25, 10, 20]

dp = [0] * n  # DP 테이블 초기화

if len(stair) <= 2:  # dp ps step 1 : 가장 작은범위 문제 해결 : 계단이 2개 이하이면 그냥 다 더해서 출력하면 됨.
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2, n):  # dp recurrence relation : DP점화식
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[-1])






####################################################################################
### dp문제 : 첫 번째, 두 번째가 채워진 dp 리스트에 대해 세 번째를 어떻게 만족시킬 것인지,그게 네 번째 ###
### 까지 보장을 해주는지에 집중해서 푸는것을 시도하기.                                        ###
#########################################ㅎ###########################################