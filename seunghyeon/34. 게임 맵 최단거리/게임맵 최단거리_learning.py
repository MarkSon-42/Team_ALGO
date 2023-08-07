# 다른분의 코드 많이 참고, 공부중

from collections import deque

def bfs(maps):
    cnt = 1
    q = deque()
    max_x, max_y = len(maps), len(maps[0])
    q.append([max_x-1, max_y-1, cnt])
    maps[max_x-1][max_y-1] = 0
    
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x == 0 and new_y == 0:
                return cnt + 1
            if 0 <= new_x < max_x and 0 <= new_y < max_y:
                if maps[new_x][new_y] != 0:
                    maps[new_x][new_y] = 0
                    q.append([new_x, new_y, cnt + 1])

    return -1

def solution(maps):
    answer = bfs(maps)

    return answer
