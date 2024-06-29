# sliding window

import sys
from collections import deque
sys.stdin = open('input1.txt', 'r')

N, Q, K = map(int, input().split())
facil_arr = list(map(int, input().split()))
facil_range = []

for _ in range(Q):
    s, e = map(int, input().split())
    facil_range.append([s, e])
#
# print(facil_arr)
# print(facil_range)

