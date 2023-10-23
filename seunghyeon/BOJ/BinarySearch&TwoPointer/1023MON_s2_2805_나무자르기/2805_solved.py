import sys
my_input = sys.stdin.readline

n, m = map(int, my_input().split())
trees = list(map(int, my_input().split()))
left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for tree in trees:
        if tree >= mid:
            total += tree - mid

    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
