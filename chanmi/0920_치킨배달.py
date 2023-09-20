import sys
from heapq import heappush
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 단축키의 개수
N, M = map(int, input().split())
city_list = [[0] * (N + 1) for _ in range(N + 1)]
house_list = []
chicken_list = []


for i in range(N):
    city_list[i + 1] = [0] + list(map(int, input().split()))

for i in range(N + 1):
    for j in range(N + 1):
        if city_list[i][j] == 1:
            house_list.append((i, j))
        elif city_list[i][j] == 2:
            chicken_list.append((i, j))

# print(house_list)
# print(chicken_list)

if M >= len(chicken_list):
    distance_list = []
    for house in house_list:
        tmp_list = []
        for chicken in chicken_list:
            heappush(tmp_list, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
        distance_list.append(tmp_list[0])
    result = sum(distance_list)
    print(result)

else:
    chicken_temp_list = list(combinations(chicken_list, M))
    final_result = []
    for combi in chicken_temp_list:
        distance_list = []
        for house in house_list:
            tmp_list = []
            for chicken in combi:
                heappush(tmp_list, abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
            distance_list.append(tmp_list[0])
        result = sum(distance_list)
        heappush(final_result, result)
    print(final_result[0])