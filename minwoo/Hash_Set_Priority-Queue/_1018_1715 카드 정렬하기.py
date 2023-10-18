import heapq
import sys

input = sys.stdin.readline

n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

answer = 0

while len(cards) > 1:
    smallest = heapq.heappop(cards)
    nextsmallest = heapq.heappop(cards)
    answer += smallest + nextsmallest
    heapq.heappush(cards, smallest + nextsmallest)

print(answer)
