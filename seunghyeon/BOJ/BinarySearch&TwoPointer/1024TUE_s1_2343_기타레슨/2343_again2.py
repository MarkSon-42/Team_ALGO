import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())  # n: 강의 수, m: blue-ray 수
lessons = list(map(int, my_input().split()))

left, right = 1, sum(lessons)
while left <= right:
	mid = (left+right) // 2
	lesson_idx = 0
	blue_ray_cnt, over = 1, 0
	for blue_ray in range(m):
		cnt_break = 0
		tmp_mid = mid
		if lesson_idx == n:
			blue_ray_cnt -= 1
			break
		while tmp_mid >= lessons[lesson_idx]:  # 처음에 조건을 while tmp_mid > 0 이라고 썼었음
			tmp_mid -= lessons[lesson_idx]
			if lesson_idx == n-1:
				cnt_break = 1
				break
			lesson_idx += 1
		if cnt_break == 0 and lesson_idx < n:
			blue_ray_cnt += 1
			if blue_ray_cnt > m:
				over = 1
				break
		else:
			break

	if blue_ray_cnt <= m:
		ans = mid
		right = mid - 1
	else:
		left = mid + 1

print(ans)
