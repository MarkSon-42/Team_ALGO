from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 1
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