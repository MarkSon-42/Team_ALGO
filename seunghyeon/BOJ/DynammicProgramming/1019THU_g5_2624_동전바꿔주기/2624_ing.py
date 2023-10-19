# 11:15
import heapq as hq
import sys
my_input = sys.stdin.readline

t = int(my_input())
k = int(my_input())
coins = [list(map(int, my_input().split())) for _ in range(k)]

coins.sort(key=lambda x: x[0], reverse=True)
# coins.insert(0, [0, 0])


for i in range(k):
	cur_coin_sum = coins[i][0] * coins[i][1]
	while coins[i][1] > 0:
		if cur_coin_sum > t:
			coins[i][1] -= 1
			cur_coin_sum -= coins[i][0]
		else:



# new_study & reminding
	# map()은 이터레이터이다.