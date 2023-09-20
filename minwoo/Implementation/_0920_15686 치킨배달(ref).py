# 삼성 SW 역량테스트 기출...

# 참고사항 : 삼성 test환경에서는 itertools 허용안된다고 함..



# n이 작아서 완탐이 가능하다.
# 치킨집들을 돌면서 거리를
# 치킨거리
# dist = abs(r1-r2) + abs(c1-c2)

# 아직 너무너무 어렵다.............

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
house, chickens = [], []
answer = 100000000
for row in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for col in range(N):
        if arr[col] == 1:
            house.append([row, col])
        if arr[col] == 2:
            chickens.append([row, col])

for chicken in combinations(chickens, M):
    total = 0
    for r, c in house:
        distance = N ** 2
        for s, e in chicken:
            distance = abs(s - r) + abs(e - c) if distance >= abs(s - r) + abs(e - c) else distance
        total += distance
    answer = min(answer, total)
print(answer)