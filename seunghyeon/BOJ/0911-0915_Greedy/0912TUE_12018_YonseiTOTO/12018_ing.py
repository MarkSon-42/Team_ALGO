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

# < heap 사용하여 k번째 최솟값 구하기 연습 >

# import heapq
#
# def find_kth_min(nums, k):
# 	heap = []
# 	for num in nums:
# 		heapq.heappush(heap, num)
#
# 	kth_min = None
# 	for _ in range(k):
# 		kth_min = heapq.heappop(heap)
# 	return kth_min
#
# print(find_kth_min([4, 1, 7, 3, 8, 5], 3))

# reference: https://kjhoon0330.tistory.com/entry/Python-heapq-%EB%AA%A8%EB%93%88#6.%20[%EC%9D%91%EC%9A%A9]%20%EC%B5%9C%EB%8C%80%20%ED%9E%99

	points = sorted(points, reverse=True)
	for i in range(n):
		m -= points.pop()
		if m < 0:
			break
		subjects_num += 1

	print(subjects_num)
