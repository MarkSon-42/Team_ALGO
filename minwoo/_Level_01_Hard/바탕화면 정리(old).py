# 파일 삭제 - 가장 왼쪽 위가 0,0 - <.>   ,    <#>
# 점 왼쪽 위 격자점에서 오른쪽 아래 격자점으로 드래그
# 최소한의 거리를 가지는 배열 return
# 왼쪽 위의 좌표를 어떻게 구할까?
# 가로 세로의 최소값이  ret 1, ret 2
# 가로 세로의 최대값이 ret 3, ret 4
# 최소는 좌표평면에서 #들의 값 중에 가장 0과 가까운 좌표값이다.
# 최대는 가장 먼 값이다.
def solution(wallpaper):
    drag_start = [9999, 9999]
    drag_end = [0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if drag_start[0] > i:
                    drag_start[0] = i  # 최소 x좌표를 넣어주는 코드
                if drag_start[1] > j:
                    drag_start[1] = j
                if drag_end[0] < i:
                    drag_end[0] = i
                if drag_end[1] < j:
                    drag_end[1] = j

    # 일단 첫점은 잘 뽑힌다.

    return drag_start[0], drag_start[1], drag_end[0] + 1, drag_end[1] + 1