import sys
from heapq import heappush
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# '-'와 '|'의 크기 S (1 <= S <= 10)
# 모니터에 나타내야 할 수 N (0 <= N = 9999999999) -> 10의 자리 : int 최댓값으로 표현 불가
S, N = input().split()
S = int(S)
N = list(N)
# 가로 전체 길이는 S * 글자의 길이
# 글자 하나 당 가로 길이는 S + 3
# 세로 길이는 S * 2

real_horizon = (S + 3) * len(N)
real_vertical = S * 2 + 3

horizon = S + 2
vertical = S * 2 + 3

number_list = [[' '] * real_horizon for _ in range(real_vertical)]

# 시작지점 저장용
current_hori_pos = 0

for i in range(len(N)):
    # 쓸 수 있는 범위는 [current_hori_pos, current_hori_pos + S + 1]

    # 1일 경우
    if int(N[i]) == 1:
        for j in range(vertical):
            # 위아래 중앙 비우기
            if j == 0 or j == (vertical // 2) or j == vertical - 1:
                continue
            # 1의 경우 세로선 위치 동일
            else:
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 2인 경우
    elif int(N[i]) == 2:
        for j in range(vertical):

            # 위아래 증앙 선 긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 2의 경우 세로선 위치가 다름
            elif j < (vertical // 2):
                number_list[j][current_hori_pos + S + 1] = '|'

            elif j > (vertical // 2):
                number_list[j][current_hori_pos] = '|'
        current_hori_pos += (S + 3)

    # 3인 경우
    elif int(N[i]) == 3:
        for j in range(vertical):

            # 위아래 중앙 선긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 3의 경우 세로선 위치 동일
            else:
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)
    
    # 4인 경우
    elif int(N[i]) == 4:
        for j in range(vertical):
            # 위아래 공백
            if j == 0 or j == vertical - 1:
                continue

            # 중앙 선긋기
            elif j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'
            # 중앙선 기준으로 위쪽은 선 두개
            elif j < (vertical // 2):
                number_list[j][current_hori_pos] = '|'
                number_list[j][current_hori_pos + S + 1] = '|'

            # 중앙선 기준으로 아래쪽은 선 하나
            else:
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 5인 경우
    elif int(N[i]) == 5:
        for j in range(vertical):
            # 위아래 중앙 선 긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 5의 경우 세로선 위치가 다름
            elif j < (vertical // 2):
                number_list[j][current_hori_pos] = '|'

            elif j > (vertical // 2):
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 6인 경우
    elif int(N[i]) == 6:
        for j in range(vertical):
            # 위아래 중앙 선 긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 중앙선 기준으로 위쪽은 선 하나
            elif j < (vertical // 2):
                number_list[j][current_hori_pos] = '|'

            # 중앙선 기준으로 아래쪽은 선 두개
            elif j > (vertical // 2):
                number_list[j][current_hori_pos] = '|'
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 7인 경우
    elif int(N[i]) == 7:
        for j in range(vertical):
            # 위쪽만 선긋기
            if j == 0:
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 중앙선 및 아래쪽은 공백
            elif j == (vertical // 2)  or j == vertical - 1:
                continue
            else:
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 8인 경우
    elif int(N[i]) == 8:
        for j in range(vertical):
            # 위아래 중앙 선 긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 그외 전부 선긋기
            else:
                number_list[j][current_hori_pos] = '|'
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 9인 경우
    elif int(N[i]) == 9:
        for j in range(vertical):
            # 위아래 중앙 선 긋기
            if j == 0 or j == vertical - 1 or j == (vertical // 2):
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'

            # 중앙선 기준으로 위쪽은 선 두개
            elif j < (vertical // 2):
                number_list[j][current_hori_pos] = '|'
                number_list[j][current_hori_pos + S + 1] = '|'

            # 중앙선 기준으로 아래쪽은 선 하나
            else:
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

    # 0인 경우
    elif int(N[i]) == 0:
        for j in range(vertical):
            # 위아래 선 긋기
            if j == 0 or j == vertical - 1:
                for k in range(horizon):
                    if k == 0 or k == horizon - 1:
                        continue
                    else:
                        number_list[j][current_hori_pos + k] = '-'
                continue

            elif j == vertical // 2:
                continue
            # 그외 전부 선긋기
            else:
                number_list[j][current_hori_pos] = '|'
                number_list[j][current_hori_pos + S + 1] = '|'
        current_hori_pos += (S + 3)

for i in range(vertical):
    print(''.join(number_list[i]))