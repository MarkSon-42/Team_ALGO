# 다시 해보기

import sys

my_input = sys.stdin.readline

S = my_input().strip()
P = my_input().strip()
idx_p = 0
len_p, len_s = len(P), len(S)
copy_num = 0  # 구하고자 하는 정답 (copy 함수를 최소로 사용하는 횟수)

# S는 P를 만들기 위한 도구문자열이고 P는 만들고자 하는 목표문자열이므로 'while idx_p < len_p:'
while idx_p < len_p:
	# max_val: s 내에서 p의 부분 문자열로 사용할 수 있는 가장 긴 부분의 길이
	max_val, tmp, idx_s = 0, 0, 0
	while idx_s < len_s and idx_p + tmp < len_p:
		if P[idx_p + tmp] == S[idx_s]:  # 현재 각 위치에서 같은 문자일 경우
			tmp += 1
			max_val = max(max_val, tmp)  # max 함수를 이용하여 max_val 업데이트
		else:  # 현재 각 위치에서 다른 문자일 경우
			tmp = 0
		idx_s += 1
	idx_p += max_val  # max_val 길이 만큼은 완전히 똑같은 문자열 부분으로 그만큼 인덱스 건너뛰기
	copy_num += 1

print(copy_num)
