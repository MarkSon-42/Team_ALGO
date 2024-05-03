# 완탐 dfs같은데 은근 까다로운 구현을 아무리 해도 안됨 100라인 넘어감

# dfs + 백트래킹 문제였음..ㅜㅜㅜㅜ


# 시간초과...#
# def solve(idx):
#     if idx == n:
#         return len([True for s, w in egg if s <= 0])
#     if egg[idx][0] <= 0:
#         return solve(idx + 1)
#     if all(s <= 0 for s, w in egg):
#         return solve(idx + 1)
#     ret = 0
#     for i in range(n):
#         if i == idx or egg[i][0] <= 0:
#             continue
#         egg[idx][0] -= egg[i][1]
#         egg[i][0] -= egg[idx][1]
#         ret = max(ret, solve(idx + 1))
#         egg[idx][0] += egg[i][1]
#         egg[i][0] += egg[idx][1]
#     return max(ret, solve(idx + 1))

# n = int(input())
# egg = [list(map(int, input().split())) for _ in range(n)]
# print(solve(0))
def dfs(n, cnt):
    global ans
    if ans >= (cnt + (N - n) * 2):  # 끝까지 진행해도 정답 갱신 불가능한 경우 (가지치기)
        return

    if n == N:  # 모든 계란을 손에 들고 부딪히기 완료
        ans = max(ans, cnt)
        return

    if arr[n][0] <= 0:  # 현재 계란이 깨진경우=>다음계란으로
        dfs(n + 1, cnt)
    else:  # 현재 계란 안깨진 상태
        flag = False  # 한번도 안 부딪혔다면.. 그래도 다음 계란으로 가야함..
        for j in range(N):  # 하나씩 부딪쳐보기
            if n == j or arr[j][0] <= 0:
                continue
            flag = True
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[j][0] <= 0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if not flag:
            dfs(n + 1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 계란index, 깨진계란 개수
dfs(0, 0)
print(ans)
