from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 1  # 문제 테케 1번 표를 보면 0~1초 사이에는 아무것도 처리도 X ->
    # gpt :  불연속 시간 간격을 처리할 때 1초 또는 문제 컨텍스트에 적합한 다른 임의의 시작점부터 시간 계산을 시작하는 것이 일반적
    queue = deque()

    total = truck_weights.pop(0)
    queue.append(total)

    while total > 0:

        answer += 1

        if len(queue) == bridge_length:
            total -= queue.popleft()

        if truck_weights and total + truck_weights[0] <= weight:
            total += truck_weights[0]
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)

    return answer

# 훨씬 빠르다.