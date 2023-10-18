import heapq
import sys

input = sys.stdin.readline

answer = 0
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
heapq.heapify(cards)

# print(cards)
while len(cards) > 1:
    minheap = heapq.heappop(cards)
    minheap2nd = heapq.heappop(cards)
    answer += minheap + minheap2nd
    heapq.heappush(cards, minheap, minheap2nd)

print(answer)