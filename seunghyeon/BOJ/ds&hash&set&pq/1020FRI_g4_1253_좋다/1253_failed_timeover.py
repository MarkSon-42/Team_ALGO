# failed: time over

import sys
my_input = sys.stdin.readline

n = int(my_input())
nums = list(map(int, my_input().split()))
nums.sort()

len_nums = len(nums)
cnt = 0
for i in range(len_nums):
	tmp = nums[:i]
	good = 0
	for l in range(i-1):
		for r in range(l, i):
			if tmp[l] + tmp[r] == nums[i]:
				cnt += 1
				good = 1
				break
		if good == 1:
			break

print(cnt)
