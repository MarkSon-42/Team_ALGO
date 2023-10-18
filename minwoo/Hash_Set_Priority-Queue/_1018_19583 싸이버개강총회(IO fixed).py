import sys

input = sys.stdin.readline

answer = 0
s, e, q = list(input().split())
s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])

attendents = {}

while True:
    input_data = input().strip()
    if not input_data:
        break

    time, name = list(map(str, input_data.split()))
    time_rec = int(time[:2] + time[3:])

    if time_rec <= s:
        attendents[name] = 1
    elif name in attendents and e <= time_rec <= q:
        attendents[name] += 1

for k, v in attendents.items():
    if v > 1:
        answer += 1

print(answer)
