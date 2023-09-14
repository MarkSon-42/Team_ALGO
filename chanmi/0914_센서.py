import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 센서의 개수
N = int(input())

# 집중국의 개수
K = int(input())


sensor_list = list(map(int, input().split()))

if K >= N:
    print(0)
else:
    sensor_list.sort()
    diff_list = [0] * (N - 1)

    for i in range(N - 1):
        diff_list[i] = sensor_list[i + 1] - sensor_list[i]

    diff_list.sort()

    for i in range(K - 1):
        diff_list.pop()

    print(sum(diff_list))