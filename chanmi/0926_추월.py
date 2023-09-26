import sys
from heapq import heappush
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 차의 대수 N
# 1 <= N <= 1000
N = int(input().strip())

car_in = [0] * N
car_out = [0] * N
count = 0

# 진입한 순서
for i in range(N):
    car_in[i] = input().strip()

# 나온 순서
for i in range(N):
    car_out[i] = input().strip()


# 진입 순서를 나온 순서와 비교
out_index = 0
in_index = 0

# 이미 추월한 차량은 비교대상에서 제외해야 하기 때문에 추월 차량 저장하는 리스트
over_car = []

while(True):

    # 차량을 다 돈 경우 종료
    if out_index == len(car_out):
        break
   
    # 이미 추월한 차랑은 진입 차량 비교대상에서 제외
    if (car_in[in_index] in over_car) and (in_index < len(car_in)):
        in_index += 1
        continue
    
    # 진입 차량과 순서가 같은 경우(추월 X)
    if car_out[out_index] == car_in[in_index]:
        in_index += 1
        out_index += 1
        continue

    # 진입 차량과 순서가 다른 경우(추월 O)
    else:
        over_car.append(car_out[out_index])
        count += 1
        out_index += 1
        continue

print(count)