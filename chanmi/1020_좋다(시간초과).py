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

number_list = []
for i in range(N):
    if i == 0:
        number_list.append(A_i[i])
    elif i == 1:
        number_list.append(A_i[i])
        number_list.append(A_i[i] + A_i[i - 1])
    else:
        tmp_list = []
        for j in range(len(number_list)):
            if number_list[j] + A_i[i] not in number_list:
                tmp_list.append(number_list[j] + A_i[i])

        number_list += tmp_list

number_list = number_list[2:]

count = 0
for num in A_i:
    if num in number_list:
        count += 1

print(count)