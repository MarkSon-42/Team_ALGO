# deque 자체가 양방향 큐
# 이걸 순환으로 구현해주면 된다
# 다만, 뽑을 요소위치의 인덱스상 거리에 따라서 큐를 반으로 나누었을 때
# 2번 명령이 빠를지, 3번 명령이 빠를지 판단하여 처리한다.

from collections import deque
import sys

n, m = map(int, input().split())

queue_idx = list(map(int, input().split()))

queue = deque([i for i in range(1, n + 1)])

count = 0

for idx in queue_idx:
    while True:
        if queue[0] == idx:
            queue.popleft()
            break
        else:
            if queue.index(idx) < len(queue)/2:
                while queue[0] != idx:
                    queue.append(queue.popleft())  # 2번째 명령
                    count += 1
            else:
                while queue[0] != idx:
                    # In deque.. appendleft(), extendleft()...
                    queue.appendleft(queue.pop())  # 3번째 명령
                    count += 1

print(count)
