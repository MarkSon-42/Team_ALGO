import sys
from heapq import heappush, heappop
from collections import deque
from itertools import combinations
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


S, E, Q = input().rstrip().split()

# 개강총회를 시작한 시간 S
start_h, start_m = map(int, S.split(":"))
start_total = start_h * 60 + start_m

# 개강총회를 끝낸 시간 E
end_h, end_m = map(int, E.split(":"))
end_total = end_h * 60 + end_m

# 개강총화 스트리밍을 끝낸 시간 Q
str_h, str_m = map(int, Q.split(":"))
str_total = str_h * 60 + str_m

before_chat = set()
end_chat = set()
while True:
    sentence = input().rstrip()
    if sentence == "":
        break

    else:
        time, name = sentence.split()
        chat_h, chat_m = map(int, time.split(":"))
        chat_total = chat_h * 60 + chat_m
        # 이전에 들어왔는지 시간 체크
        if chat_total <= start_total:
            before_chat.add(name)
        # 끝날때 채팅 친 시간 확인
        elif end_total <= chat_total and chat_total <= str_total:
            end_chat.add(name)

# 참여자 수 체크
count = 0

for id in before_chat:
    if id in end_chat:
        count += 1
    else:
        continue

print(count)