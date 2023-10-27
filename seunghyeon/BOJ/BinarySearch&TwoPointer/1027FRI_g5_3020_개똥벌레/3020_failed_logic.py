# even == odd 일 때 어떻게 l, r을 업데이트 해줘야할지 모르겠었음
# tc1은 맞으나 역시지능나 tc2는 안됨

import heapq as hq
import sys
my_input = sys.stdin.readline

n, h = map(int, my_input().split())

lst = [int(my_input().rstrip()) for i in range(n)]

cnt_lst = []
l, r = 1, h
lst_len, cnt_lst_len = len(lst), 0
while l <= r:
	m = (l+r) // 2
	now_cnt, even, odd = 0, 0, 0
	for i in range(lst_len):
		if i % 2 == 0:
			if m <= lst[i]:
				now_cnt += 1
				even += 1
		else:
			if m > h-lst[i]:
				now_cnt += 1
				odd += 1
	hq.heappush(cnt_lst, [now_cnt, m])
	cnt_lst_len += 1
	if even >= odd:
		l = m + 1
	else:
		r = m - 1
	# 같을 땐 어떡하지?

min_val = cnt_lst[0][0]
section = 0
idx = 0
while idx < cnt_lst_len:
	if cnt_lst[idx][0] != min_val:
		break
	section += 1
	idx += 1

print(min_val, section)
