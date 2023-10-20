import sys
from queue import PriorityQueue
from collections import deque
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 수의 개수 N (1 <= N <= 2000)
N = int(input().rstrip())

A_i = list(map(int, input().rstrip().split()))
A_i.sort()

# N^2 시간복잡도 사용 불가.
count = 0

for i in range(N):
    target = A_i[i]
    start = 0
    end = len(A_i) - 1

    while start < end:
        if A_i[start] + A_i[end] == target:
            # 앞에 숫자 두 개 제외
            if start == 1:
                start += 1
            
            # 자기 자신 제외
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif A_i[start] + A_i[end] > target:
            end -= 1
        elif A_i[start] + A_i[end] < target:
            start += 1