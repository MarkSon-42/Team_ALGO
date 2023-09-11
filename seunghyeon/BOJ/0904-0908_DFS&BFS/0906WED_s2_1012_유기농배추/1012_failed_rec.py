import sys
input = sys.stdin.readline
# sys.setrecursionlimit(52*2)

def find_earthwarms_num(x, y, earthwarm_num):
    visited[x][y] = True

    for i in range(4):
        new_x, new_y = x + move_x[i], y + move_y[i]
        if field[new_x][new_y] == 1 and not visited[new_x][new_y]:
            find_earthwarms_num(new_x, new_y, earthwarm_num)
        else:
            continue
    earthwarm_num += 1

    return earthwarm_num

# '위, 아래, 왼, 오' 순서
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    col, row, cabbage_num = map(int, input().split())
    field = [[0] * (row + 2) for _ in range(col + 2)]
    visited = [[False] * (row + 2) for _ in range(col + 2)]

    for _ in range(cabbage_num):
        x, y = map(int, input().split())
        field[x + 1][y + 1] = 1

    earthwarm_num = 0
    for x in range(1, col + 1):
        for y in range(1, row + 1):
            if field[x][y] == 1 and field[x - 1][y] == 0 and field[x][y - 1] == 0 and not visited[x][y]:
                earthwarm_num = find_earthwarms_num(x, y, earthwarm_num)

    print(earthwarm_num, "\n")


# 마주했던 ERROR : Recursion error
    # sys.setrecursionlimit(52*2) 를 사용하려했지만 좋은 방법이 아님! -> Stack을 사용하는 로직 다시 짜보자