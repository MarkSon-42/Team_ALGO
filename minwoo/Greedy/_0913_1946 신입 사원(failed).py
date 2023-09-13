# boj 1946
import sys
input = sys.stdin.readline
T = int(input())
cand_list = []
for _ in range(T):
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        cand_list.append((A, B))
        for j in range(len(cand_list)):
            pass

print(cand_list)