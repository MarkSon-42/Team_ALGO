# 횡단보도 1 ~ 100,000

import sys
input = sys.stdin.readline

answer = 0
brokenLight = [i for i in range(1, n + 1)]



n, k, b = map(int, input().split())

for i in range(k):
    if brokenLight[i] == -1:
        answer += 1

tmp = answer

# 지난번에도 썼던 슬라이딩 윈도우
for i in range(1, n - k + 1):
    if brokenLight[i - 1] == -1:
        tmp -= 1
    if brokenLight[i + k - 1] == -1:
        tmp += 1

    answer = min(answer, tmp)

print(answer)