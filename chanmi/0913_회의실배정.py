import sys
from collections import Counter

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
room_list = [[] for _ in range(N)]
for i in range(N):
    room_list[i] = list(map(int, input().split()))

room_list.sort(key=lambda x:(x[1], x[0]))

end_time = room_list[0][1]
room_count = 1

for i in range(1, N):
    if room_list[i][0] >= end_time:
        room_count += 1
        end_time = room_list[i][1]


print(room_count)