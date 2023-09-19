import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input().rstrip())
	observations = [list(map(int, my_input().split())) for _ in range(N)]
	observations = sorted(observations, key=lambda x: x[0])

	len_obs, cnt = len(observations), 0
	for idx in range(1, len_obs):
		if observations[idx][0] == observations[idx-1][0]:
			if observations[idx][1] != observations[idx-1][1]:
				cnt += 1
	print(cnt)
