import sys

my_input = sys.stdin.readline

n, m = map(int, my_input().split())
time = list(map(int, my_input().split()))

s, e = max(time), sum(time)

while s <= e:
	mid = (s + e) // 2
	total, cnt = 0, 1
	for t in time:
		if total + t > mid:
			cnt += 1
			total = 0
		total += t

	if cnt <= m:
		ans = mid
		e = mid - 1
	else:
		s = m + 1

print(ans)
