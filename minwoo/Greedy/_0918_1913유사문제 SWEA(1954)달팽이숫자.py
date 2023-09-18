import sys

sys.stdin = open("input.txt", "r")

t = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for test_case in range(1, t + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    i, j, cnt, dr= 0, 0, 1, 0
    arr