# time over code

import sys
my_input = sys.stdin.readline

trees_dic = {}
total = 0
while 1:
	tree = my_input().rstrip()
	if tree == '':
		break
	if tree in trees_dic:
		trees_dic[tree] += 1
	else:
		trees_dic[tree] = 1
	total += 1

keys = sorted(list(trees_dic.keys()))
for key in keys:
	print(key+"{: .4f}".format(trees_dic[key]/total * 100))
	# 왜 key + 가 아니라 key, 로 쓰면 key와 숫자 사이에 공백이 두 개가 되는가? -> 출력오류 떴음
