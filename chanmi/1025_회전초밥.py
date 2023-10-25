import sys
from queue import PriorityQueue
from collections import deque
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 회전 초밥 벨트에 놓인 접시의 수 N (2 <= N <= 30000)
# 초밥의 가지수 d (2 <= d <= 3000)
# 연속해서 먹는 접시의 수 k (2 <= k <= 3000 (k <= N))
# 쿠폰 번호 c (1 <= c <= d)
N, d, k, c = map(int, input().split())

sushi = []

for i in range(N):
    num = int(input().rstrip())
    sushi.append(num)

# 투포인터 문제
left = 0
right = 0
count = 0

while left != N:
    right = left + k
    kind = set()
    is_add = True
    for i in range(left, right):
        i %= N
        kind.add(sushi[i])
        if sushi[i] == c:
            is_add = False
        number = len(kind)
        if is_add:
            number += 1
            count = max(number, count)
            left += 1

print(count)
