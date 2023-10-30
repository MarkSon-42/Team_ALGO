import sys
my_input = sys.stdin.readline

k, n = map(int, my_input().split())
cables = [int(my_input().rstrip()) for _ in range(k)]

left, right = 1, max(cables)
while left <= right:
	mid = (left+right) // 2
	now_cnt = 0
	for cable in cables:
		if cable >= mid:
			now_cnt += cable // mid
	if now_cnt >= n:
		left = mid + 1
	else:
		right = mid - 1

print(right)
