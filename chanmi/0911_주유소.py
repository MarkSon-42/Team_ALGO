import sys

# N이 1000인 경우 M이 499500이라는 최악의 숫자가 나올 수 있어서
# 재귀 깊이를 설정해주고 readline을 쓰는 게 속도 줄여줌
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 도시 개수
N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

price = cost[0]
distance = road[0] * price

for i in range(1, N - 1):
    if cost[i] < price:
        price = cost[i]
    distance += price * road[i]
        
print(distance)