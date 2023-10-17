import sys
my_input = sys.stdin.readline


def set_seat(p_info, p_board, p_n):
	candidate_seats1, candidate_seats2, candidate_seats3 = [], [], []
	max_favorite_num, now_favorite_num = 0, 0
	for col in range(1, p_n+1):
		for row in range(1, p_n+1):
			if p_board[col][row] == 0:
				now_favorite_num = 0
				#조건1에 맞게 이번 자리 고르기 -> 골라서 후보 list 안에 저장
				if p_board[col-1][row] != 0 and p_board[col-1][row] in p_info[1:]:
					now_favorite_num += 1
				if p_board[col+1][row] != 0 and p_board[col+1][row] in p_info[1:]:
					now_favorite_num += 1
				if p_board[col][row-1] != 0 and p_board[col][row-1] in p_info[1:]:
					now_favorite_num += 1
				if p_board[col][row+1] != 0 and p_board[col][row+1] in p_info[1:]:
					now_favorite_num += 1

				if now_favorite_num >= max_favorite_num:
					max_favorite_num = now_favorite_num
					candidate_seats1.append([col, row])
	# 적합한 자리가 딱 한 개이면
	if len(candidate_seats1) == 1:
		x, y = candidate_seats1[0][0], candidate_seats1[0][1]
		p_board[x][y] = p_info[0]
		return p_board
	# 적합한 자리가 두 개 이상 -> 조건 2 검사
	else:
		max_empty_num, now_empty_num = 0, 0
		for s1 in candidate_seats1:
			# 조건 2에 맞는 칸들만 남기기
			if p_board[s1[0]-1][s1[1]] == 0 and s1[0]-1 >= 1 and s1[1] and s1[0]-1 <= N and s1[1] <= N:
				now_empty_num += 1
			if p_board[s1[0]+1][s1[1]] == 0 and s1[0]+1 >= 1 and s1[1] and s1[0]+1 <= N and s1[1] <= N:
				now_empty_num += 1
			if p_board[s1[0]][s1[1]-1] == 0 and s1[0] >= 1 and s1[1]-1 and s1[0] <= N and s1[1]-1 <= N:
				now_empty_num += 1
			if p_board[s1[0]][s1[1]+1] == 0 and s1[0] >= 1 and s1[1]+1 and s1[0] <= N and s1[1]+1 <= N:
				now_empty_num += 1
			if now_empty_num >= max_empty_num:
				max_empty_num = now_empty_num
				candidate_seats2.append(s1)

				# 적합한 자리가 딱 한 개이면
				if len(candidate_seats2) == 1:
					x, y = candidate_seats2[0][0], candidate_seats2[0][1]
					p_board[x][y] = p_info[0]
					return p_board
			# 적합한 자리가 두 개 이상 -> 조건 3 검사
			else:
				candidate_seats2 = sorted(candidate_seats2, key=lambda a: (a[1], a[0]))
				x, y = candidate_seats2[0][0], candidate_seats2[0][1]
				p_board[x][y] = p_info[0]
	return p_board


if __name__ == "__main__":
	N = int(my_input())
	board = [[0] * (N+2) for _ in range(N+2)]

	student_num = N**2
	infos = []
	satisfactions = [[] for _ in range(student_num)]
	for s in range(student_num):
		info = list(map(int, my_input().split()))
		infos.append(info)
		satisfactions[s].append(info[0])
		board = set_seat(info, board, N)
	dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
	satisfaction, i = 0, 0
	for col in range(1, N+1):
		for row in range(1, N+1):
			# board[col][row]를 반복문돌려 찾는 방법밖에생각안남. 코드그만짜고 다른분 코드보고 공부하고 나중에 다시 짜보도록하자.
			if board[col-1][row] in infos[i][1:]:
				satisfaction += 1
			if board[col+1][row] == 0:
				satisfaction += 1
			if board[col][row-1] == 0:
				satisfaction += 1
			if board[col][row+1] == 0:
				satisfaction += 1




		# 만족도 합산하기
	print(satisfaction)
