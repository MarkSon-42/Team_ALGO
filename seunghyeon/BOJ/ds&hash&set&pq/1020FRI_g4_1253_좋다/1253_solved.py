# 투 포인터를 활용하여 더욱 효율적으로 바꿈
# 입력값으로 음수가 들어오는 경우를 고려안했어서, 음수도 고려하여 코드 수정

import sys
my_input = sys.stdin.readline

n = int(my_input())
nums = list(map(int, my_input().split()))
nums.sort()

len_nums = len(nums)
cnt = 0
for i in range(len_nums):
	tmp = nums[:i] + nums[i+1:]
	l, r = 0, len_nums - 2
	while l < r:
		sum = tmp[l] + tmp[r]
		if sum == nums[i]:
			cnt += 1
			break
		if sum < nums[i]:
			l += 1
		else:
			r -= 1

print(cnt)
