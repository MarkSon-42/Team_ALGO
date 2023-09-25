# 코트에 나온 문제랑 거의 같음
# 안쪽 배열들도 회전해야 함
n, m, rotation = tuple(map(int, input().split()))
start = 1
# 시작 배열 초기화
answer = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        answer[i][j] = start
        start += 1

# rotation만큼 회전하기

for _ in range(rotation):
    # 안쪽 회전할 사각형
    inner = min(n, m) // 2
    for j in range(inner):
