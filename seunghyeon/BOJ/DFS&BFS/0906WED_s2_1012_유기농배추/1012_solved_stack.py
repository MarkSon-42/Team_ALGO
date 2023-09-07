# 자고나서 또 풀어보기!!

import sys
from collections import deque

input = sys.stdin.readline

# '위, 아래, 왼, 오' 순서
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def find_earthworms_num(x, y):
    visited[x][y] = True
    stack = deque([(x, y)])

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            new_x, new_y = cx + move_x[i], cy + move_y[i]
            if field[new_x][new_y] == 1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                stack.append((new_x, new_y))

T = int(input())
for _ in range(T):
    col, row, cabbage_num = map(int, input().split())
    field = [[0] * (row + 2) for _ in range(col + 2)]
    visited = [[False] * (row + 2) for _ in range(col + 2)]

    for _ in range(cabbage_num):
        x, y = map(int, input().split())
        field[x + 1][y + 1] = 1

    earthworm_num = 0
    for x in range(1, col + 1):
        for y in range(1, row + 1):
            if field[x][y] == 1 and not visited[x][y]:
                find_earthworms_num(x, y)
                earthworm_num += 1

    print(earthworm_num)