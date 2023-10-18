# score: 100
# 이런 아이디어 생각하는 연습하기
# two-pointer 방식으로도 풀어보기 (조금 더 빠름)

import sys
my_input = sys.stdin.readline

n = int(my_input())
m = int(my_input())
s = my_input()

cursor, ioi_cnt, rst_cnt = 0, 0, 0
while (cursor + 2) <= (m - 1):
	if s[cursor: cursor+3] == "IOI":
		ioi_cnt += 1
		cursor += 2
		if ioi_cnt == n:
			rst_cnt += 1
			ioi_cnt -= 1
	else:
		cursor += 1
		ioi_cnt = 0

print(rst_cnt)
