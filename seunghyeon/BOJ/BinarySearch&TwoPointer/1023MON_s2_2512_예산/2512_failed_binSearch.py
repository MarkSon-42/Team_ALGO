import sys
my_input = sys.stdin.readline

n = int(my_input())  # 지방의 수
requests = list(map(int, my_input().split()))
requests.sort()
total_amount = int(my_input())

s, e = 0, max(requests)
now_sum = 0
if sum(requests) >= e:
	print(max(requests))
else:
	m = 0
	while s <= e:
		m = (s+e) // 2
		now_sum = 0
		for request in requests:
			now_sum += min(m, request)
		if now_sum > total_amount:
			e = m - 1
		else:
			s = m + 1
	print(m)
