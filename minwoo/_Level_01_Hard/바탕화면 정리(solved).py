#  예전에 쉽게 풀었던.. 근데 다시 풀어야

#  문자열 배열   빈칸 -> .      파일   -> #

#  (0, 0)   (세로 좌표, 가로 좌표)

#  드래그 하기 S(start), E(end)

#  점 S(lux, luy)에서 점 E(rdx, rdy)로 드래그를 할 때,

#  "드래그 한 거리"는 |rdx - lux| + |rdy - luy|로 정의합니다.

#  한번의 드래그로 모든 파일을 삭제할 수 있게끔

# 결국 드래그 시작 좌표 & 끝 좌표를 구하는 문제

# lux , luy, rdx, rdy -> ....> x_min y_min x_max y_max

def solution(wallpaper):
    lux, luy, rdx, rdy = 999, 999, -999, -999
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#' and i < lux:
                lux = i  # start의 세로 좌표 구하기 (최소값)
            if wallpaper[i][j] == '#' and j < luy:
                luy = j  # start의 가로 좌표 구하기 ( - )
            if wallpaper[i][j] == '#' and i > rdx:
                rdx = i  # end의 세로 최대 좌표
            if wallpaper[i][j] == '#' and j > rdy:
                rdy = j  # end의 가로 최대 좌표

    return [lux, luy, rdx + 1, rdy + 1]

#  한번 틀린 코드 -> return [lux, luy, rdx, rdy]
#  좌표와 배열 칸은 다르다. 이를 고려하지 않고 출력해서 틀렸었음...