# BFS를 써보자
# 출발 노드를 deque에 넣기
# 방향 탐색 -> dx, dy
# while로 큐를 돈다 -> 큐가 빌때까지 계속 돌게 loop
# 이전에 풀었던.. 문제랑 비슷한데 기억이..(방위탐색) -> 스터디때 푼건 아닌 것 같음

from collections import deque

def solution(maps):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]
    row = len(maps)
    col = len(maps[0])

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()  # 참고.. pop()은 list크기에 따라서 O(N), popleft()는 O(1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:  # 맵 범위 체크 ( 이 조건문도 거의 패턴.. )
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1  # 이전 블럭에서 +1 이게 곧 거리 계산
                    queue.append((nx, ny))

    if maps[row - 1][col - 1] != 1:
        return maps[row - 1][col - 1]
    else:
        return -1