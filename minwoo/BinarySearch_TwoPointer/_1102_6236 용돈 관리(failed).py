# 그나마 입력값들의 범위가 매우매우 적은 편이다.
# 아마 이분탐색 말고 또 다른걸로도 풀 수도 있을 듯..?

import sys

input = sys.stdin.readline

n, m = map(int, input().split())


amounts = [int(input()) for i in range(n)]

lower_bound = 1
upper_bound = 100000

while lower_bound <= upper_bound:
    mid = (lower_bound + upper_bound) // 2
    money = mid
    count = 1

    for a in amounts:
        if money - a < 0:
            pass
