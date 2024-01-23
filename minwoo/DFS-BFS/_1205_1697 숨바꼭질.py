from collections import deque

MAX_INT = 10 ** 5
dist = [0] * (MAX_INT + 1)
# dist 변수는 시작점 n에서 각 위치까지의 최단 거리를 저장하는 배열

n, k = map(int, input().split())
def bfs():
    q = deque()  # deque() 큐를 초기화 하기
    q.append(n)  # 큐의 시작점을 append()로 deque에 추가.
    #  q = [5]
    while q:
        curr_pos = q.popleft()
        # curr_pos = 5
        if curr_pos == k:
            print(dist[curr_pos])
            break
        for next_pos in (curr_pos - 1, curr_pos + 1, curr_pos * 2):
            # for ~ next_pos = 5 - 1, 5 + 1, 5 * 2
            # next_pos 4, 6, 10
            if 0 <= next_pos <= MAX_INT and not dist[next_pos]:
                dist[next_pos] = dist[curr_pos] + 1
                q.append(next_pos)

bfs()

# n = 5, k = 17