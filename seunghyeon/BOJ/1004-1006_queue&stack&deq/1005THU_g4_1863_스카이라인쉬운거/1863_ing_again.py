import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	n = int(my_input())
	skylines = list(map(int, my_input().split())[1] for _ in range(n))
	skylines.append(0)

	stk = [0]
	building_num = 0
	for skyline in skylines:
		height = skyline
