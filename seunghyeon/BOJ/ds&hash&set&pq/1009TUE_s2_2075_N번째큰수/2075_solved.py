import heapq
import sys
my_input = sys.stdin.readline

N = int(my_input())
heap = []

for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < N: # heap의 크기는 n 유지하기
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
