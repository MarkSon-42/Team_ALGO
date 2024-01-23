from collections import deque

def solution(order):
    answer = 0
    length = len(order)
    main_belt = deque([i for i in range(1, length + 1)])
    sub_belt = []
    for i in range(order[0] - 1):
        if main_belt:
            sub_belt.append(main_belt.popleft())

    for box in order:
        if main_belt and box == main_belt[0]:
            main_belt.popleft()
            answer += 1
        elif sub_belt and box == sub_belt[-1]:
            sub_belt.pop()
            answer += 1
        else:
            break

    return answer

solution([5, 4, 3, 2, 1])