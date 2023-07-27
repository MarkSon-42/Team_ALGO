# DFS, BFS가 그냥 그래프의 동작 흐름만 생각나고 코드로 구현을 못하겠다..
# ㅜㅡㅜ..




# BFS 풀이
from collections import deque
# 'deque'는 BFS 순회에 더 효율적인 양방향 대기열을 만드는 데 사용

def solution(numbers, target):
    cnt = 0
    queue = deque()
    # 초기상태 ((sum = 0, index = 0)) 초기화 : 루트 노드에서 BFS 탐색
    queue.append((0, 0))
    while queue: #  queue가 비어있지 않으면 계속 루프
        current_sum, index = queue.popleft()

        if index == len(numbers):
            if current_sum == target:
                cnt += 1
        else:
            current_number = numbers[index]
            queue.append((current_sum + current_number, index + 1))
            queue.append((current_sum - current_number, index + 1))

    return cnt


# 대박 신기한 풀이.. ( 완탐 )

from itertools import product

def solution2(numbers, target):
    pass