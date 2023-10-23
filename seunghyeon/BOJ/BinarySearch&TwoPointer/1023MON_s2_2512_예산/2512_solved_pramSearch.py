# 10:10 ~ 10:25

import sys
my_input = sys.stdin.readline

n = int(my_input())  # 지방의 수
requests = list(map(int, my_input().split()))
requests.sort()
total_amount = int(my_input())

assignment = []
printing = 0
for request in requests:
	upper_limit = total_amount // n
	if request <= upper_limit:
		assignment.append(request)
		total_amount -= request
		n -= 1
	else:
		printing = 1
		print(upper_limit)
		break

if printing == 0:
	print(max(assignment))


# 매개변수 탐색(Parametric Search)란?
	# 조건을 만족하는 최대값을 구하기