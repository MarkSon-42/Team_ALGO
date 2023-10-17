import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	towers = list(map(int, my_input().split()))
	stk = []
	answer = [0 for _ in range(N)]

	for i in range(N):
		while stk:
			if stk[-1][1] > towers[i]:
				answer[i] = stk[-1][0] + 1
				break
			else:
				stk.pop()
		stk.append([i, towers[i]])

	# print(' '.join(map(str, answer)))
	print(*answer)

# 새로 공부한 것: 가변인자를 사용하여 프린트하기
# 배운 아이디어: 모든 tower마다 남은 tower들을 다 비교해줘서 시간초과났었는데, 비교할 필요 없는 대상들은 미리 제거해버리기