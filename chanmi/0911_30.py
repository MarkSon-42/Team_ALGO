import sys

sys.setrecursionlimit(10**6)

# 도시 개수
N = list(input())
N.sort(reverse=True)
N = ''.join(N)
N = int(N)

if N % 30 == 0:
    print(N)
else:
    print(-1)