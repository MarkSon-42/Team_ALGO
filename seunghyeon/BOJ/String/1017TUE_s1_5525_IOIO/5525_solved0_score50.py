# sub task question, score: 50

import sys
my_input = sys.stdin.readline

n = int(my_input().rstrip())
m = int(my_input().rstrip())
s = my_input().rstrip()

io = 'IO'
ioi = [io for _ in range(n)]
ioi.append('I')
ioi_str = ''.join(ioi)

first_idx, last_idx = 0, len(s)-1
for c in s:
	if c != 'I':
		first_idx += 1
	else:
		break
for c in s[-1:]:
	if c != 'I':
		last_idx -= 1
	else:
		break
s = s[first_idx: last_idx+1]
len_s, len_ioi = len(s), len(ioi_str)
idx, cnt = 0, 0
last_start = len_s - len_ioi + 1
while idx <= last_start:
	if s[idx] == 'I':
		if ioi_str == s[idx:idx+len_ioi]:
			cnt += 1
			idx += 2
		else:
			idx += 1
	else:
		idx += 1

print(cnt)


