# BF 하면 시간초과
# DP풀이를 참고..
# https://only-wanna.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0-%ED%92%80%EC%9D%B4

def solution(land):
    # dp테이블 초기화
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    for i in range(len(land)):
        if i == 0:
            dp[0] = land[0]
            continue
        for j in range(4):
            dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])
    return max(dp[-1])


# 아직도 DP를 한번에 떠올리고 구현하지 못하겠다..