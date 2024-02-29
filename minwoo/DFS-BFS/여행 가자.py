# 새로 배운 알고리즘 : 유니온 파인드

import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

N = int(input())
M = int(input())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

matrix = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

for i in range(N):
    for j in range(i, N):
        if matrix[i][j] == 1:
            union(i + 1, j + 1)

for i in range(M - 1):
    if find(plan[i]) != find(plan[i + 1]):
        print("NO")
        exit(0)

print("YES")