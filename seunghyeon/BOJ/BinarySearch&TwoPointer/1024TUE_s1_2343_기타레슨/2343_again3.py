# 9:30 ~ 10:10 / 2343 내가 직접 푼 코드 중 가장 깔끔한 정답코드인 것 같음
import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
lessons = list(map(int, my_input().split()))

s, e = 1, sum(lessons)
while s <= e:
	mid = (s+e) // 2
	blue_ray_cnt, idx = 1, 0
	for blue_ray in range(m+1):
		if idx == n:
			blue_ray_cnt -= 1
		if blue_ray_cnt > m or idx == n:
			break
		tmp_mid = mid
		while tmp_mid >= lessons[idx]:
			tmp_mid -= lessons[idx]
			if idx == n-1:
				idx += 1
				break
			idx += 1
		blue_ray_cnt += 1

	if blue_ray_cnt <= m:
		e = mid - 1
	else:
		s = mid + 1

print(s)
