import sys
from queue import PriorityQueue
from collections import deque
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 카드 묶음 수 N (1 <= N <= 100000)
N = int(input().rstrip())

card_list = PriorityQueue()

for i in range(N):
    card_num = int(input().rstrip())
    card_list.put(card_num)

count = 0
while card_list.qsize() != 1:
    first_card = card_list.get()
    second_card = card_list.get()
    current_count = first_card + second_card
    count = count + current_count
    card_list.put(current_count)

print(count)