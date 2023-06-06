def solution(park, routes):
    h, w = len(park), len(park[0]) # 세로, 가로 길이
    grid = [[0 for j in range(w)] for i in range(h)] # 공원 배열 생성
    current_row, current_col = 0, 0 # 초기 위치 설정
    for i in range(h):
        for j in range(w):
            if park[i][j] == "X": # 장애물은 공원배열에 1로 표시
                grid[i][j] = 1
            elif park[i][j] == "S": # S 시작점을 현재 위치로 초기화
                current_row, current_col = i, j
    
    dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)} # 동서남북 방향 정의
    for route in routes:
        direction, distance = route.split() # 방향, 거리 받기
        dir_row, dir_col = dirs[direction] 
        check = True
        
        for k in range(1, int(distance) + 1):
            new_row, new_col = current_row + dir_row * k, current_col + dir_col * k # 다음 위치를 현재 위치에서 방향 * 거리로 표현
            if new_row in range(h) and new_col in range(w) and grid[new_row][new_col] == 0: # 공원 배열이나 장애물이 없는 곳이면 pass, 아니면 check를 false 처리해서 반복종료
                pass
            else:
                check = False
                break
        if check: # check가 true이면 현재 위치를 다음 위치로 이동
            current_row, current_col = new_row, new_col
    
    return[current_row, current_col] # 세로 방향 좌표, 가로 방향 좌표로 return