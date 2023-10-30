import sys
my_input = sys.stdin.readline

N, M = map(int, my_input().split())
trees = list(map(int, my_input().split()))

s, e = 0, max(trees)
while s <= e:
	m = (s+e) // 2
	now_sum = 0
	for t in trees:
		if t - m > 0:
			now_sum += (t - m)
	if now_sum >= M:  # 여기 부등호가 >로 해야할지 >=로 해야할지 생각을 잘 못했었음. 잘 생각하기.
		s = m + 1
	else:
		e = m - 1

print(e)
