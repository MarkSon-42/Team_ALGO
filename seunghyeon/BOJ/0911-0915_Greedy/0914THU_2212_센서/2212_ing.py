# 18:10 - 18:30 /
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input().rstrip())
	K = int(my_input().rstrip())
	sensors = sorted(list(map(int, my_input().split())))
	diss = []
	for i in range(len(sensors)-1):
		diss.append(sensors[i+1]-sensors[i])
	diss = sorted(diss)
	print(sum(diss[:-K+1]))

# 뭐가 틀린지 모르겠음.. 보류