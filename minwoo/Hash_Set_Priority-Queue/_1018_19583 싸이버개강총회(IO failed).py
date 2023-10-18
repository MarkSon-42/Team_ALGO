# 입장 확인 여부 체크

# 대화 여부 체크

# 입퇴장 모두 체크된

import sys
input = sys.stdin.readline

answer = 0
s, e, q = list(input().split())
s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])

attendents = {}

while True:
    time, name = list(map(str, input().split()))
    time_rec = int(time[:2] + time[3:])

    if time_rec <= s:
        attendents[name] = 1
    elif name in attendents and e <= time_rec <= q:
        attendents[name] += 1

for k, v in attendents.items():
    if v > 1:
        answer += 1


print(answer)