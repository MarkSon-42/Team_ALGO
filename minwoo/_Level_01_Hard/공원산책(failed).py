def solution(park, routes):
    row = 0
    col = 0
    # 출발점 부터 찾아주기.
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                row, col = i, j
                break

    move = 0

    for c in routes:
        if 'E' in c:
            move = int(c[2])

    # ....???? 문제에 쓴대로 쭉 구