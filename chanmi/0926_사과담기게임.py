import sys
from heapq import heappush
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 스크린 사이즈와 바구니 크기
# 1 <= M < N <= 10
N, M = map(int, input().split())

# 떨어지는 사과 개수
# 1 <= J <= 20
J = int(input().strip())

# 현재 바구니의 왼쪽 끝, 오른쪽 좌표 끝를 저장
if M > 1:
    current_pos = [1, M]
else:
    current_pos = [1, 1]

apple_fall = [0] * J

for i in range(J):
    apple_fall[i] = int(input().strip())

# 움직인 횟수
count = 0

for pos in apple_fall:

    # 바구니의 왼쪽 좌표보다 작은 경우 왼쪽으로 이동
    if pos < current_pos[0]:
        diff = current_pos[0] - pos
        count += diff
        current_pos[0] -= diff
        current_pos[1] -= diff
    # 바구니의 오른쪽 좌표보다 큰 경우 오른쪽으로 이동
    elif pos > current_pos[1]:
        diff = pos - current_pos[1]
        count += diff
        current_pos[0] += diff
        current_pos[1] += diff
    # 동일할 경우 움직이지 않음(범주에 이미 들어있는 경우도 포함)
    elif pos == current_pos[0] or pos == current_pos[1]:
        continue

print(count)