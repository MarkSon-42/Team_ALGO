# 1 0 마킹을 반대로? -> 빈구간

#

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M ,K = map(int, input().split())

# 방향 설정 -> 상하좌우 .. 팔방일 경우 예전문제 있음.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):

