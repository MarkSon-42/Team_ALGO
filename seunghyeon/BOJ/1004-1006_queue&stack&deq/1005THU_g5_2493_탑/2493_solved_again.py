import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input())
	towers = list(map(int, my_input().split()))

	stk = []
	answer = [0] * N
	for i in range(N):
		while stk:
			if stk[-1][1] > towers[i]:
				answer[i] = stk[-1][0] + 1
				break
			else:
				stk.pop()
		stk.append([i, towers[i]])

	print(*answer)
