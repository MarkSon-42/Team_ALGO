# mid가 반복이 실행될 때마다 계속 1씩 내려가게 하는 실수를 저지른 코드 -> left, right가 정상적으로 업데이트 될 수 없음

import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())  # n: 강의 수, m: blue-ray 수
lessons = list(map(int, my_input().split()))

left, right = 1, 300
while left <= right:
	mid = (left+right) // 2
	lesson_idx = 0
	blue_ray_cnt = 1
	for blue_ray in range(m):
		cnt_break = 0
		while mid > 0:
			if lesson_idx == n:
				cnt_break = 1
				break
			mid -= lessons[lesson_idx]
			lesson_idx += 1
		if cnt_break == 0 and lesson_idx < n-1:
			blue_ray_cnt += 1
		else:
			break

	if blue_ray_cnt < m:
		right = mid - 1
	else:
		left = mid + 1

print(right)
