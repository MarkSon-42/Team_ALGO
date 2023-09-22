import sys
my_input = sys.stdin.readline


def mv_func(k_x, k_y, s_x, s_y, ins):
	k_x += ins[0]
	k_y += ins[1]
	if k_x <= 0 or k_y <= 0 or k_x > 8 or k_y > 8:
		k_x -= ins[0]
		k_y -= ins[1]
		return k_x, k_y, s_x, s_y
	if s_x == k_x and s_y == k_y:
		s_x += ins[0]
		s_y += ins[1]
		if s_x <= 0 or s_y <= 0 or s_x > 8 or s_y > 8:
			k_x -= ins[0]
			k_y -= ins[1]
			s_x -= ins[0]
			s_y -= ins[1]
			return k_x, k_y, s_x, s_y

	return k_x, k_y, s_x, s_y


if __name__ == "__main__":
	# 알파벳 A~H, 숫자 1~8 -> (열, 행)
	# 입력: 킹 위치, 돌 위치, 움직인 횟수 N
	king, stone, N = my_input().split()
	kx, ky = 9-int(king[1]), ord(king[0]) - ord('A') + 1
	sx, sy = 9-int(stone[1]), ord(stone[0]) - ord('A') + 1

	mv_dic = {
		'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0],
		'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]
	}
	for _ in range(int(N)):
		inst = mv_dic.get(my_input().rstrip(), (0, 0))
		kx, ky, sx, sy = mv_func(kx, ky, sx, sy, inst)
	print(chr(ky + ord('A') - 1) + str(9-kx))
	print(chr(sy + ord('A') - 1) + str(9-sx))

# 처음에 맨 밑부터 위로 1,2,3... 이렇게 거꾸로되어있는걸 놓쳐서 틀림
	# 처음에 입력받을 때 king과 stone의 x좌표를 9-int(king[1]) 이런식으로 설정해줌으로써 실제 좌표값으로 계산을 해준 뒤
	# 마지막에 출력할 때 str(9-kx) 이런식으로 다시 9- 를 해줌으로써 원하는 답이 출력되도록 함