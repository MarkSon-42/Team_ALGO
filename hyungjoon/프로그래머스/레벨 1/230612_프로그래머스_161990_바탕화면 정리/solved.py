'''
문제 : 바탕화면 정리
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161990
'''
import sys

def solution(wallpaper):
    answer = []
    
    # 1. 파일이 등장할 때, lx, ly좌표와 rx, ry좌표를 각각 최소/최대에 맞게 갱신해준다.
    # 2. 해당 범위 안에 파일 갯수를 충족한다면 lx, ly, rx, ry 를 return 해준다.
    # 3. 이 때, rx, ry 값은 파일이 등장한 좌표의 +1, +1 만큼 해줘야 그 파일을 포함하여 드래그가 가능하다.
    
    lx, ly, rx, ry = sys.maxsize, sys.maxsize, 0, 0
    
    # 파일이 나타날 때마다 lx, ly, rx, ry 값을 갱신해준다.
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lx = min(lx, i)
                ly = min(ly, j)
                rx = max(rx, i+1)
                ry = max(ry, j+1)
    
    answer = [lx, ly, rx, ry]
    
    return answer

solution([".#...", "..#..", "...#."])