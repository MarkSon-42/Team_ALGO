import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
heights = list(map(int, input().split()))
rain = [0] * N
drain = [0] * N

for i in range(M):
    s, e = map(int, input().split())
    for j in range(s-1, e):
        rain[j] += 1
    if (i+1) % 3 == 0:
        for j in range(max(0, s-3), min(N, e+2)):
            if rain[j] > 0:
                rain[j] -= 1
                drain[j] += 1

for i in range(N):
    heights[i] += rain[i] + drain[i]

for height in heights:
    print(height)

# 하... 이거 아님

