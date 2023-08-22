from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    answer = 0
    while bridge_queue:
        answer += 1
        bridge_queue.popleft()
        if truck_queue:
            if sum(bridge_queue) + truck_queue[0] <= weight:
                bridge_queue.append(truck_queue.popleft())
            else:
                bridge_queue.append(0)
    return answer


# 아마 while안에 sum()때문에 시간초과 나는듯.