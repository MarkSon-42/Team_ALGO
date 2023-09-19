# 유사문제 : SWEA 1954   https://www.youtube.com/watch?v=rw2gQg9x_EA

# boj 1913 달팽이 s3


# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-1913-%EB%8B%AC%ED%8C%BD%EC%9D%B4-Brute-Force

n = int(input())
num = int(input())

matrix = [[0] * n for _ in range(n)]

# 방향 벡터 (up, down, left, right)

direct_x = [-1, 1, 0, 0]
direct_y = [0, 0, -1, 1]

matrix_num = n * n
i, j = 0, 0   # 현재 세로(행)인덱스, 가로(열) 인덱스
direction = 0

