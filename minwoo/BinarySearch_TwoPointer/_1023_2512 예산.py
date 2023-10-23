# 나무 자르기랑 매우 유사한데
# 이 문제는 이해가 감
# 근데 나무자르기는 아직 이해 안됨..
# 코딩 테스트 이분탐색 문제가
# 정렬이 되어있지 않은 경우
# end를 max()로 깔고가는 건가..?

# n이 1만개 밖에 안되어 정렬해서 품.
import sys

input = sys.stdin.readline

n = int(input())

budget = list(map(int, input().split()))

m = int(input())

budget.sort()

start = 1
end = budget[-1]

answer = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for b in budget:
        if b > mid:
            total += mid
        else:
            total += b

    if total <= m:
        start = mid + 1
        result = mid

    else:
        end = mid - 1
print(answer)