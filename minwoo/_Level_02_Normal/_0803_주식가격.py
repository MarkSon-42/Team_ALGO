# 큐

from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        p = q.popleft()
        sc = 0
        for t in q:
            sc += 1
            if p > t:
                break

        answer.append(sc)
    return answer

# queue -> O(N**2)

# stack이 더 좋다는데..