import heapq
import sys
my_input = sys.stdin.readline

N = int(my_input())
b = []

for _ in range(N):
	b.append(map(int, my_input().split()))
heapq.heapify(b)

for i in range(4):
	rst = heapq.heappop(b)

print(b[0])

