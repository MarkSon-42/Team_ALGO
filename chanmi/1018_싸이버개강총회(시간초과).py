import sys
from heapq import heappush, heappop
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


S, E, Q = input().rstrip().split()

# 개강총회를 시작한 시간 S
start_h, start_m = S.split(":")

# 개강총회를 끝낸 시간 E
end_h, end_m = E.split(":")

# 개강총화 스트리밍을 끝낸 시간 Q
str_h, str_m = Q.split(":")

before_chat = []
end_chat = []

while True:
    sentence = input().rstrip()
    if sentence == "":
        break

    else:
        time, name = sentence.split()
        chat_h, chat_m = time.split(":")
        # 이전에 들어왔는지 시간 체크
        if chat_h < start_h:
            before_chat.append(name)
        elif chat_h == start_h and chat_m <= start_m:
            before_chat.append(name)
        
        # 끝날때 채팅 친 시간 확인
        elif chat_h < str_h and (chat_h >= end_h and chat_m >= end_m):
            end_chat.append(name)
        elif chat_h <= str_h and chat_m <= str_m and (chat_h >= end_h and chat_m >= end_m):
            end_chat.append(name)

# 참여자 수 체크
count = 0
people = []

for id in before_chat:
    if id in end_chat:
        count += 1
        people.append(id)
    else:
        continue

print(count)