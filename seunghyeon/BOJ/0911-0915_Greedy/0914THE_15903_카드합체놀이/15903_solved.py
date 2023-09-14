import heapq
import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())

cards = []
inputs = [int(x) for x in my_input().split()]

for card in inputs:
    heapq.heappush(cards, card)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))

