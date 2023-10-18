import sys

my_input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

attend = {}
cnt = 0
while True:
	chat_record = my_input().split()
	if len(chat_record) < 2:
		break
	chat_time, name = chat_record[0], chat_record[1]
	time = int(chat_time[:2]+chat_time[3:])

	if time <= start:
		attend[name] = 1
	elif end <= time <= stream and name in attend:
		attend[name] += 1

for k, v in attend.items():
	if v >= 2:
		cnt += 1

print(cnt)
