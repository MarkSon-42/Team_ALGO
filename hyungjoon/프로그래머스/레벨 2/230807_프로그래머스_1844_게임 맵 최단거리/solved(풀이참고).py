'''
문제 : 게임 맵 최단거리
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''
from collections import deque

def solution(maps):
    answer = 0
    
    # 1. 시뮬레이션 + bfs로 풀기
    
    # 상하좌우
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx, ny = x + dr[i], y + dc[i]
                
                # 맵을 벗어나는건 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                    
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                    
                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
                    
        # 상대 팀 진영(제일 오른쪽 아래 칸) 까지 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    
    return -1 if answer == 1 else answer

print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))