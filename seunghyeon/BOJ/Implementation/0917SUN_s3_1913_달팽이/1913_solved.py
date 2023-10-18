import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input().rstrip())
	target = int(my_input().rstrip())
	target_x, target_y = 0, 0

	x_direct = [1, 0, -1, 0]  # down, right, up, left
	y_direct = [0, 1, 0, -1]
	direct_idx = 0  # down, right, up, left

	board = [[0] * N for _ in range(N)]
	x, y, first_num = 0, 0, N**2
	go_cnt = N

	for _ in range(N):
		rep = 2
		if go_cnt == N:
			rep = 1
		for r in range(rep):
			for cnt in range(go_cnt):
				board[x][y] = first_num
				if first_num == target:
					target_x = x
					target_y = y
				first_num -= 1
				if cnt == go_cnt - 1:
					direct_idx += 1
				x = x + x_direct[direct_idx % 4]
				y = y + y_direct[direct_idx % 4]
		go_cnt -= 1

	str_board = []
	for b in board:
		str_board.append(list(map(str, b)))
	for str_b in range(N):
		print(' '.join(str_board[str_b]))

	print(target_x+1, target_y+1)


# 한 두 번 도는거 판단해줄 때 for문말고 if문으로 %, // 등 조건걸기 활용하기
#그리고 이번처럼 1,2,2,2,... 번 반복해야할 때 (첫번째만 다르다던가 그런 경우) 무조건 큰 for문안에 모든게 돌아가도록 if문 지저분하게 설정할 수도 있지만
	# 첫 번째꺼만 따로 빼서 하고 같은 번수만큼 돌아야하는 것들에 대해서만 for문 돌리는 것도 괜찮을 듯
