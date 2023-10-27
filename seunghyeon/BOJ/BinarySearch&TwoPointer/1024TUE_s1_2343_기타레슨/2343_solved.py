import sys

my_input = sys.stdin.readline

n, m = map(int, my_input().split())
lessons = list(map(int, my_input().split()))

s, e = max(lessons), sum(lessons)

while s <= e:
	mid = (s + e) // 2
	total, cnt = 0, 1
	for lesson in lessons:
		if total + lesson > mid:
			cnt += 1
			total = 0
		total += lesson
	if cnt <= m:
		ans = mid
		e = mid - 1
	else:
		s = m + 1

print(ans)
