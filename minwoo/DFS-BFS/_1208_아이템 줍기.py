# 제출된 코드 중 좋은 풀이 찾음

# 4방향
dij = [0, -1, 0, 1, 0]
# 좌표계를 2배율로 늘려 구성
rects = [[0] * 102 for _ in range(102)]


# 모서리 판별
def is_corner(x, y):
    if not rects[y][x] == 1: return False
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if not rects[i][j]: return True
    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 사각형 찍기
    for square in rectangle:
        ix, iy, ex, ey = square
        for i in range(iy * 2, ey * 2 + 1):
            for j in range(ix * 2, ex * 2 + 1):
                rects[i][j] = 1

    # BFS
    q = [(0, 0) for _ in range(800)]
    q[0] = (characterX * 2, characterY * 2)
    rects[q[0][1]][q[0][0]] = 2  # 사각형과 구분한 visited 처리를 위해 2 더해줌

    ptr, tg = 1, 0
    while ptr != tg:
        qx, qy = q[tg][0], q[tg][1]
        for k in range(4):
            tx, ty = qx + dij[k], qy + dij[k + 1]
            if is_corner(tx, ty):
                q[ptr] = (tx, ty)
                rects[ty][tx] = rects[qy][qx] + 0.5  # 2배율이므로 거리를 0.5씩 가산
                ptr += 1
        tg += 1

    return rects[itemY * 2][itemX * 2] - 2  # 최종 계산에서 2를 차감
