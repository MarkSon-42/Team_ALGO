import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	T = int(my_input())

	for tc in range(T):
		n1, n2 = my_input().split()

		if n1 == '0' and n2 == '0':
			print(0)

		else:
			len_n1, len_n2 = len(n1), len(n2)
			if len_n1 != 80:
				n1 = '0'*(80-len_n1)+n1
			if len_n2 != 80:
				n2 = '0'*(80-len_n2)+n2

			rst_num = []
			tmp = 0
			for idx in range(80):
				now_sum = int(n1[79-idx])+int(n2[79-idx])+tmp
				if now_sum <= 1:
					rst_num.append(str(now_sum))
					tmp = 0
				elif now_sum == 2:
					rst_num.append('0')
					tmp = 1
				elif now_sum == 3:
					rst_num.append('1')
					tmp = 1

				if tmp == 1 and idx == 79:
					rst_num.append('1')

			# len_rst_num = len(rst_num)
			# for c in range(len_rst_num):
			# 	if rst_num[len_rst_num-1-c] == '0':
			# 		rst_num.pop()
			# 	else:
			# 		break

			while rst_num:
				if rst_num[-1] == '0':
					rst_num.pop()
				else:
					break
			print(''.join(rst_num[::-1]))


# 이 파일에서 틀린부분은 38번째줄부터의 내용입니다.
# pop을 사용하지 않는 방식으로 바꿨더니 통과를했고 이 코드를 제출하면 25퍼센트에서 failed가 납니다.
# 차라리 아예 틀리면 모르겠는데 문제에서 준 테스트케이스나 질문게시판에 올라온거는 다 돼서 뭐가 잘못된건지 모르겠습니다
# 스터디 전에 이 파일을 보시는 분이계시다면 뭐가 잘못된거고 어떻게 수정해야 통과를받을지 함께고민해보고 스터디시간에 얘기해주세요 ㅠㅠㅠ