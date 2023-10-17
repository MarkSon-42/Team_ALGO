import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	N = int(my_input().rstrip())
	dis_lst = list(map(int, my_input().split()))
	cost_lst = list(map(int, my_input().split()))

	min_cost = cost_lst[0]
	total_cost = 0

	for i in range(N-1):
		min_cost = cost_lst[i] if min_cost > cost_lst[i] else min_cost
		total_cost += min_cost*dis_lst[i]
	print(total_cost)
