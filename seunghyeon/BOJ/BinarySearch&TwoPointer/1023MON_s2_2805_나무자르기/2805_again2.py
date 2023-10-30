import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
trees = list(map(int, my_input().split()))

left, right = 1, max(trees)
while left <= right:
	mid = (left+right) // 2
	now_sum = 0
	for tree in trees:
		if tree - mid > 0:
			now_sum += (tree-mid)
	if now_sum >= m:
		left = mid + 1
	else:
		right = mid - 1

print(right)
