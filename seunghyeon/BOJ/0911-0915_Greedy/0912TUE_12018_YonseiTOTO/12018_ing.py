import heapq
import sys
my_input = sys.stdin.readline

if __name__ == "__main__":
	n, m = map(int, my_input().split())
	points = []
	subjects_num = 0
	for i in range(n):
		apply_num, limit_num = map(int, my_input().split())
		each_point_lst = sorted(list(map(int, input().split())))
		if apply_num >= limit_num:
			for _ in range(apply_num-limit_num):
				heapq.heappop(each_point_lst)
			points.append(heapq.heappop(each_point_lst))
		else:
			points.append(1)

	points = sorted(points, reverse=True)
	for i in range(n):
		m -= points.pop()
		if m < 0:
			break
		subjects_num += 1

	print(subjects_num)
