# sub task question, score: 50, 1 percent increase
# if s[r_idx] == 'I' ---> if s[r_idx] == 'I' and s[l_idx] == 'I'

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
r_idx, cnt = 0, 0
last_start = len_s - len_ioi
while r_idx <= last_start:
	l_idx = r_idx + len_ioi - 1
	if s[r_idx] == 'I' and s[l_idx] == 'I':
		if ioi_str == s[r_idx:l_idx+1]:
			cnt += 1
			r_idx += 2
		else:
			r_idx += 1
	else:
		r_idx += 1

print(cnt)
