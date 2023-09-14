import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

for i in range(M):
    card_list.sort()
    card_result = card_list[0] + card_list[1]
    card_list[0] = card_list[1] = card_result

print(sum(card_list))