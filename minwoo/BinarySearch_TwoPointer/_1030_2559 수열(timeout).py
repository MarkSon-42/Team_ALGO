# 부분합을 반복문 돌려야 하나 싶었는데
# 그냥 sum()에 슬라이싱 하면 그만임..!
# 근데, 테케는 다 맞는데 시간초과..  O(N)이라서? 아니면 무한루프?
# gpt : O(N)아니고,  N과 K가 아주 큰 경우 O(N*K) = O(N^2)임...
# n : 2 ~ 100,000
# k : 1 ~ n
# elem :  -100 ~ 100

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

days = list(map(int, input().split()))

left = 0
right = k - 1
max_sum = 0

# print(sum(days[left:right + 1]))

while right < n - 1:
    partial_sum = sum(days[left:right + 1])
    if max_sum <= partial_sum:
        max_sum = partial_sum
    left += 1
    right += 1

print(max_sum)