import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree_heights = list(map(int, input().split()))

th_len = len(tree_heights)

left, right = 1, max(tree_heights)
while left <= right:
    log_sum = 0
    mid = (left + right) // 2
    for t in tree_heights:
        if t > mid:
            log_sum += t - mid

    if log_sum < m:
        right = mid - 1
    else:
        left = mid + 1
print(right)
