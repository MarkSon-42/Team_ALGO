# 5분컷
# 그러나 온라인에선 도무지 투포인터와 이분탐색에 대한 제대로된
# 설명을 찾을 수가 없다..
# mid의 설정 여부말고 차이점이 없는 듯

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

wear = list(map(int, input().split()))
wear.sort()
left, right = 0, n - 1
cnt = 0
while wear[left] < wear[right]:
    _sum = wear[left] + wear[right]
    if _sum < m:
        left += 1
    elif _sum == m:
        cnt += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(cnt)