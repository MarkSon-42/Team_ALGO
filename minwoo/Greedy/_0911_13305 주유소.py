import sys
input = sys.stdin.readline


N = int(input())

roadway = list(map(int, input().split()))

cost = list(map(int, input().split()))

# 그리디 .. 첫 번째 값 설정

min_val = roadway[0] * cost[0]

# 가장 저렴한 주유소

min_cost = cost[0]

# IndexError ..

# N -> N - 1로 해줘야 out of range 방지
for i in range(1, N - 1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    min_val += min_cost * roadway[i]

print(min_val)