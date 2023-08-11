# 시간초과가 걸려있는 문제
# 1. 탐색 범위를 줄여보자
# 2. 연산의 횟수를 줄여보자

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    queue1_sum, queue2_sum = sum(queue1), sum(queue2)

    for i in range(len(queue1) * 3):  # 왜 len q1의 3배만큼 도는지 근거를 모르겠음..
        if queue1_sum == queue2_sum:
            return i
        if queue1_sum < queue2_sum:
            popped = queue2.popleft()
            queue1_sum += popped
            queue2_sum -= popped
            queue1.append(popped)
        else:
            popped = queue1.popleft()
            queue1_sum -= popped
            queue2_sum += popped
            queue2.append(popped)
    return -1

