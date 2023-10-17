import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	T = int(my_input())

	for tc in range(T):
		n1, n2 = my_input().split()

		len_n1, len_n2 = len(n1), len(n2)
		if len_n1 != 80:
			n1 = '0'*(80-len_n1)+n1
		if len_n2 != 80:
			n2 = '0'*(80-len_n2)+n2

		rst_num = []
		tmp = 0
		for idx in range(79, -1, -1):
			now_sum = int(n1[idx]) + int(n2[idx]) + tmp
			if now_sum == 0:
				rst_num.append('0')
				tmp = 0
			elif now_sum == 1:
				rst_num.append('1')
				tmp = 0
			elif now_sum == 2:
				rst_num.append('0')
				tmp = 1
			elif now_sum == 3:
				rst_num.append('1')
				tmp = 1

			if tmp == 1 and idx == 0:
				rst_num.append('1')

			rst_num = rst_num[::-1]
			len_rst_num = len(rst_num)
			for c in range(len_rst_num):
				if rst_num[c] == '0':
					continue
				else:
					break
			print(''.join(rst_num[c:]))

# failed 파일에서 개선된 부분: 36번째 줄부터
	# 개선사항: pop해서 0을 없애주는 대신 '0'아 아니게 되는 지점을 찾아주기만 한 뒤 그 지점부터만 join해주는 로직으로 바꿈